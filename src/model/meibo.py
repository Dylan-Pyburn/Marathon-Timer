from collections import defaultdict
import csv

REQUIRED_FIELDS = ['組','番号','区別','苗字','名前']


class MeiboFieldnameError(Exception):
    def __init__(self, message):
        super().__init__(message)

class MeiboDataError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Meibo:
    '''
    Students can be uniquely identified by (class, number)
    '''

    def __init__(self, path:str=''):
        '''
        Constructor. Takes a string that is a path to a CSV file.
        '''
        self.set_path(path)
        self.is_loaded:bool = False

        self.lines    : list = []  # the lines of the meibo file as stripped strings
        self.csv_rows : list = []  # using this for formatting rows
        self.data     : list = {}  # the parsed data from the meibo file

    def set_path(self, path:str) -> None:
        '''
        Set the path to the meibo file.
        Must be a CSV file.
        '''
        # must be a string
        if not isinstance(path, str):
            raise TypeError(f'Meibo: path must be a {str}, but was {type(path)}')
        
        # can be blank, otherwise must be a CSV
        if not path == '' and  not path.split('.')[-1] == 'csv':
            raise ValueError('Meibo path must be a csv file.')
        
        self.path = path

    def clear(self) -> None:
        '''
        DELETE ALL LINES AND DATA, as well as the path.
        '''
        self.path = ''
        self.lines.clear()
        self.csv_rows.clear()
        self.data.clear()
        self.is_loaded = False
    
    def load(self) -> str:
        '''
        Read data from the file located at the set path.
        Verify that the required fields are presents, no data is missing, 
        and no students are repeated.
        Return blank string if success, otherwise error message.
        '''
        # read the meibo file twice.
        #  - once to get the lines as strings
        #  - once to get use csvreader

        # lines from csv file
        lines = self._read_csv_lines()
               
        # get the csv data
        fieldnames, csv_rows = self._read_csv_data()

        # verify the data
        self._check_file_format(fieldnames, csv_rows)

        # everything looks good, parse the data and
        # commit the data to the class variables
        self.lines     = lines
        self.csv_rows  = csv_rows
        self.data      = self._parse_data(csv_rows)
        self.is_loaded = True

    #=============================================
    #       Data Access
    #=============================================

    def lookup(self, studentClass:str, studentNumber:str=None) -> dict:
        if not studentClass in self.data:
            return None
        
        classData = self.data[studentClass]
        
        studentData = None
        if studentNumber in classData:
            studentData = classData[studentNumber]

        if studentNumber:
            return studentData
        else:
            return classData
        

    def get_data(self, sortmode='newest'):
        raise NotImplementedError

    def get_path(self) -> str:
        '''
        Return the path to the meibo file.
        '''
        return self.path

    def get_classes(self) -> list:
        '''
        Return a list containing all classes present in the meibo.
        '''
        return [k for k  in self.data]

    def get_students(self, studentClass:str) -> list:
        '''
        Return a dictionary who's keys are student numbers
        and values are dictionaries of student data.
        '''
        self._check_student_class(studentClass)
        return self.data[studentClass]

    def get_lines(self):
        '''
        Return a list containing the raw lines from the meibo file.
        '''
        return self.lines
    
    def get_formatted_lines(self):
        lines = []
        for line in self.csv_rows:
            values = [line[field] for field in REQUIRED_FIELDS]
            kumi, number, gender, lname, fname = values
            lines.append(f'{kumi} {number} {gender} {lname} {fname}')
        
        for line in lines:
            print(line)

        return lines
    
    @staticmethod
    def row_to_str(row):
        '''
        TODO
        A static implementation of the above method, similar to how it is in EntryModel.
        Can be implemented after sorting is implemented
        '''
        raise NotImplementedError

    def get_data(self):
        '''
        Return the dictionary of processed meibo data:
        Keys are 組.
        Values are dictionaries whose keys are 番号 
        and values are student name and gender.
        '''
        return self.data

    #=============================================
    #       Data Validation
    #=============================================

    def _check_student_class(self, studentClass:str):
        # studentClass must be a string and be in the dictionary
        if not isinstance(studentClass, str):
            raise TypeError(f'studentClass should be {str}, was {type(studentClass)}')
        if not studentClass in self.data:
            raise KeyError(f'Meibo: class "{studentClass}" is not in the meibo')
        
    def _check_student_number(self, studentClass:str, studentNumber:str):
        # if provided, studentNumber should be string, and be in the class
        if studentNumber and not isinstance(studentNumber, str):
            raise TypeError(f'studentNumber should be {str}, was {type(studentNumber)}')
        if studentNumber and not studentNumber in self.data[studentClass]:
            raise KeyError(f'Meibo: class "{studentClass}" has no student number "{studentNumber}"')
    
    def _parse_data(self,  rows:list):
        '''
        Parse the DictReader data into a dictionary.
        '''
        data  = defaultdict(dict)
        for row in rows:
            data[row['組']][row['番号']] = {
                '区別': row['区別'],
                '苗字': row['苗字'],
                '名前': row['名前']
            }
        return data

    def _read_csv_lines(self) -> list:
        '''
        Return the raw lines of the csv file as a list of strings.
        '''
        lines = []
        with open(self.path, mode='r', encoding='utf-8') as infile:
            for line in infile.readlines():
                lines.append(line.rstrip())
        return lines

    def _read_csv_data(self) -> tuple:
        '''
        Return the DictReader data of the csv file as a list of dictionaries.
        '''
        fieldnames, csv_rows = [], []
        with open(self.path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            fieldnames = csv_reader.fieldnames
            for row in csv_reader:
                csv_rows.append(row)
        return (fieldnames, csv_rows)
          
    def _check_file_format(self, fieldnames:list, rows:list):
        '''
        fieldnames: a list of strings.
        rows: a list of dictionaries (from csv.Dictreader)
        '''
        # the meibo may have other fields, but the required ones must be included
        self._check_fieldnames(fieldnames)

        # make sure that all the data is there for every row
        self._check_for_missing_data(rows)

        # students cannot be entered more than once
        self._check_for_double_entries(rows)

    def _check_fieldnames(self, fieldnames):
        '''
        Raise MeiboFieldnameError if a required fieldname is missing.
        '''
        for field in REQUIRED_FIELDS:
            if not field in fieldnames:
                raise MeiboFieldnameError(f'{field} must be a field in the meibo')
            
    def _check_for_missing_data(self, rows:list):
        '''
        Raise MeiboDataError if a rows is missing a field.
        '''
        for i, row in enumerate(rows):
            for value in row.values():
                if value  == None:
                    rowstr = Meibo.row_to_string(row)
                    raise MeiboDataError(f'Meibo: row {i} is missing data: {rowstr}')
        
    def _check_for_double_entries(self, rows:list):
        '''
        Raise MeiboDataError if any (組, 番号) pair is repeated.
        '''
        # originally did this my making a set of (組, 番号) pairs and comparing the length to rows,
        # but I wanted to easily provide the offending line so I changed it
        #students = set((row['組'], row['番号']) for row in rows)
        students = defaultdict(int)
        for row in rows:
            kumi, number = row['組'], row['番号']
            students[(kumi, number)] += 1
        for k, v in students.items():
            if v > 1:
                kumi, number = k
                raise MeiboDataError(f'Meibo:「組:{kumi}, 番号:{number}」である生徒は2人以上いが入っています')
