import csv
import datetime as dt

from src.model.meibo import Meibo

TEMP_DIR = './temp'

ENTRY_FIELDS = ['区別','順位','組','番号','苗字','名前']

class EntryDataError(Exception):
    def __init__(self, message):
        super().__init__(message)

class EntryManager:
    '''
    Entries can be uniquely identified by (gender, rank)
    '''

    def __init__(self):
        self.temp_path = None
        self.save_path = None
        self.meibo     = None
        self.data      = []  # keys are (class, number) pairs
        
        self._init_temp_file()

    def set_meibo(self, meibo):
        if not isinstance(meibo, Meibo):
            raise TypeError(f'Entry: meibo must be of type {Meibo}')

        self.meibo = meibo        

    #=============================================
    #       File Operatations
    #=============================================

    def set_save_path(self, path:str):
        '''
        Set the path to the file that entries will be saved to.
        Must be a CSV file.
        '''
        # must be a string
        if not isinstance(path, str):
            raise TypeError(f'Entry: path must be a {str}, but was {type(path)}')
        
        # can be blank, otherwise must be a CSV
        if not path == '' and  not path.split('.')[-1] == 'csv':
            raise ValueError('Entry path must be a csv file.')
        
        self.path = path
    
    def _init_temp_file(self):
        # set the filename for the temp file
        t = dt.datetime.now()
        s = t.strftime("%Y%m%d-%H%M%S")
        self.temp_path = f'{TEMP_DIR}/{s}-entry.csv'

    def _write_data(self, sortmode='newest', temp:bool=False):
        '''
        This was the original save function, but I wanted to hide writing
        to the temp file from code that uses this object, so now only
        writing to the user-chosen save file is public.
        '''
        outpath = self.temp_path if temp else self.save_path
        
        data = self.get_entries(sortmode)
        
        with open(outpath, mode='w', newline='', encoding='utf-8') as outfile:
            csv_writer = csv.DictWriter(outfile, fieldnames=ENTRY_FIELDS)
            csv_writer.writeheader()
            csv_writer.writerows(data)
    
    def _save_temp_data(self):
        self._write_data(temp=True) 
    
    def save_data(self, sortmode='newest'):
        self._write_data(sortmode, temp=False)
    
    def load(self):
        pass
    
    def load_existing(self):
        pass
    
    #=============================================
    #       Entry Operatations
    #=============================================

    def clear(self):
        self.path = ''
        self.meibo = None
        self.data.clear()

    def add(self, studentClass:str, studentNumber:str, studentRank:str):
        self.check_entry_data(studentClass, studentNumber, studentRank)

        # no further error checking on this look feels dangerous, 
        # but at this point we do know it exists from the above check 
        studentInfo = self.meibo.lookup(studentClass, studentNumber)
        lname       = studentInfo['苗字']
        fname       = studentInfo['名前']
        gender      = studentInfo['区別']
        
        newEntry = {
            '区別'  : gender,
            '順位'  : studentRank,
            '組'    : studentClass,
            '番号'  : studentNumber,
            '苗字'  : lname,
            '名前'  : fname
        }
        self.data.append(newEntry)
        self._save_temp_data()
    
    def remove(self, entryStr):
        '''
        Entry string shall be of format;
            '区別 順位 組 番号 苗字 名前'
        '''
        _, _, studentClass, studentNumber, _, _ = entryStr.split()
        for entry in self.data:
            if entry['組'] == studentClass and entry['番号'] == studentNumber:
                break
        self.data.remove(entry)
        self._save_temp_data()

    #=============================================
    #       Data Access
    #=============================================

    def lookup(self, studentClass, studentNumber):
        for entry in self.data:
            if entry['組'] == studentClass and entry['番号'] == studentNumber:
                return entry

        return None

    def get_entries(self, sortmode:str='newest'):
        data = self.data
        
        # reversed to show the end of the list first
        if sortmode == 'newest':
            return reversed(data)
        
        # not reversed because we'll desplay in the same order added
        elif sortmode == 'oldest':
            return data

        # sort by rank, then by gender (reversed so males come first)
        # Did nested sorted() because I'm too lazy to deepcopy data
        elif sortmode == 'sortedMale':
            return sorted(sorted(data, key=lambda x: x['順位']), 
                            key=lambda x: x['区別'], reverse=True)

        # sort by rank, then by gender (females will come first)
        # Again did nested sorted() because I'm too lazy to deepcopy data
        elif sortmode == 'sortedFemale':
            return sorted(sorted(data, key=lambda x: x['順位']), 
                            key=lambda x: x['区別'])

        # just in case?
        return data

    @staticmethod
    def entry_to_str(entry:dict):
        '''
        Entry string shall be of format;
            '区別 順位 組 番号 苗字 名前'
        '''
        for field in ENTRY_FIELDS:
            if not field in entry:
                raise EntryDataError(f'entry is missing 「{field}」')

        gender = entry['区別'] 
        rank   = entry['順位']
        kumi   = entry['組']
        number = entry['番号']
        lname  = entry['苗字']
        fname  = entry['名前']
        return f'{gender:<20} {rank} {kumi} {number} {lname} {fname}' 

    def get_path(self):
        return self.path
        
    #=============================================
    #       Data Validation
    #=============================================
    
    def check_entry_data(self, studentClass, studentNumber, studentRank):
        # check that the given data is in proer format
        self._check_format('組', studentClass) 
        self._check_number_format('番号', studentNumber)
        self._check_number_format('順位', studentRank)

        # check that the data represents a nonentered student
        self._check_class_number(studentClass, studentNumber)
    
        # student does exist, so check that the (gender, rank) has not been enteres
        # perform the meibo lookup to get the gender
        student = self.meibo.lookup(studentClass, studentNumber)
        self._check_gender_rank(student['区別'], studentRank)

    
    def _check_class_number(self, studentClass, studentNumber):
        '''
        Check that this (class, number) pair is in the meibo
        and has not yet been entered.
        '''
        # check that the student exists in the meibo
        studentData = self.meibo.lookup(studentClass, studentNumber)
        if not studentData:
            raise EntryDataError(f'({studentClass}, #{studentNumber}) is not in the meibo')
         
        # check that the student is not already in the entries
        entryData = self.lookup(studentClass, studentNumber)
        if entryData:
            raise EntryDataError(f'({studentClass}, #{studentNumber}) is already entered')
    
    def _check_gender_rank(self, gender, rank):
        '''
        Check that this (gender, rank) pair has not yet been entered.
        '''
        for entry in self.data:
            if entry['区別'] == gender and entry['順位'] == rank:
                raise EntryDataError(f'順位が {rank} 番の{gender}の生徒は既に入力されました')

    def _check_format(self, field:str, value):
        # must be a string
        if not isinstance(value, str):
            raise TypeError(f'{field} should be {str}, was {type(field)}') 
        
        # must not be blank
        if value == '':
            raise ValueError(f'Entry: {field} cannot be blank')

        
    def _check_number_format(self, field:str, value):
        self._check_format(field, value)

        # must represent a positive int
        try:
            int(value)
        except ValueError:
            raise ValueError(f'Entry: {field} must be an integer')
        
        # must be positive
        if not int(value) > 0:
            raise ValueError(f'Entry: {field} must be greater than zero')


        

        

