import csv

from src.model.meibo import Meibo

ENTRY_FIELDS = ['区別','順位','組','番号','苗字','名前']

class EntryManager:
    '''
    Entries can be uniquely identified by (gender, rank)
    '''

    def __init__(self):
        '''
        Construtor.
        ''' 
        self.path  = ''
        self.meibo = None

        self.data  = []  # keys are (class, number) pairs

    def set_meibo(self, meibo):
        if not isinstance(meibo, Meibo):
            raise TypeError(f'Entry: meibo must be of type {Meibo}')

        self.meibo = meibo        

    #=============================================
    #       File Operatations
    #=============================================

    def set_path(self, path:str):
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
    
    def save(self):
        pass
    
    def load(self):
        pass
    
    def load_existing(self):
        pass
    
    #=============================================
    #       Entry Operatations
    #=============================================

    def clear(self):
        pass

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

    #=============================================
    #       Data Access
    #=============================================

    def lookup(self, studentClass, studentNumber):
        for entry in self.data:
            if entry['組'] == studentClass and entry['番号'] == studentNumber:
                return entry

        return None

    def get_entries(self, sortmode:str='newest'):
        data = self.entry_data
        
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
    def entry_to_str(self, entry:dict):
        '''
        Entry string shall be of format;
            '区別 順位 組 番号 苗字 名前'
        '''
        gender = entry['区別'] 
        rank   = entry['順位']
        kumi   = entry['組']
        number = entry['番号']
        lname  = entry['苗字']
        fname  = entry['名前']
        return f'{gender} {rank} {kumi} {number} {lname} {fname}' 

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
        TODO
          handle errors thrown by meibo
        '''
        # check that the student exists in the meibo
        self.meibo.lookup(studentClass, studentNumber)
         
        # check that the student is not already in the entries
        # self.lookup(studentClass, studentNumber)

        pass
    
    def _check_gender_rank(self, studentGender, studentRank):
        '''
        Check that this (gender, rank) pair has not yet been entered.
        '''
        pass

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


        

        

