
from collections import defaultdict
import csv

MEIBO_FIELDS = ['組','番号','性別','苗字','名前']
ENTRY_FIELDS = ['順位','組','番号','性別','苗字','名前']

class EntryModel:

    def __init__(self):
        self.meibo_path     = ''
        self.entries_path   = ''
        
        self.meibo_rows     = [] # the raw lines as read in from the csv
        self.meibo_data     = {} # parsed csv data
        
        self.entry_rows     = []
        self.entry_data     = []

    #=============================================
    #       Entries
    #=============================================        

    def save_entries(self) -> str:
        if len(self.entry_data) == 0:
            return 'there are no entries to be written'

        try:
            with open(self.entries_path, mode='w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=ENTRY_FIELDS)
                csv_writer.writeheader()
                csv_writer.writerows(self.entry_data)
            return''
        except:
            return f'couldn\'t write to file: "{self.entries_path}"'

    def get_entry_str(entry:dict) -> str:
        return f'{entry['性別']}{entry['順位']}  {entry['組']}  #{entry['番号']}  {entry['苗字']} {entry['名前']}'

    def entry_lookup(self, studentClass, studentNumber) -> dict:
        '''
        組と出席番号を使い、ある生徒の有無を入力した生徒たちから調べる

        Params:
            (str) studentClass  :  組
            (str) studentNumber :  出席番号
        Return:
            ある: dict{順位, 組, 番号, 性別,苗字, 名前}
            ない: None
        '''
        for entry in self.entry_data:
            if entry['組'] == studentClass and entry['番号'] == studentNumber:
                return entry
        return None

    def add_entry(self, studentClass, studentNumber, studentRank):
        studentInfo = self.meibo_lookup(studentClass, studentNumber)
        if studentInfo == None:
            return 

        studentFamilyName   = studentInfo['苗字']
        studentFirstName    = studentInfo['名前']
        studentGender       = studentInfo['性別']
        
        newEntry = {
            '順位'  : studentRank,
            '組'    : studentClass,
            '番号'  : studentNumber,
            '性別'  : studentGender,
            '苗字'  : studentFamilyName,
            '名前'  : studentFirstName
        }
        newEntryStr = '  '.join([v for v in newEntry.values()])

        self.entry_data.append(newEntry)
        return newEntryStr

    def get_entry_rows(self,sortmode='newest'):
        data = self.get_entries(sortmode)
        return [EntryModel.get_entry_str(entry) for entry in data]

    def get_entries(self, sortmode='newest') -> list:
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
                            key=lambda x: x['性別'], reverse=True)

        # sort by rank, then by gender (females will come first)
        # Again did nested sorted() because I'm too lazy to deepcopy data
        elif sortmode == 'sortedFemale':
            return sorted(sorted(data, key=lambda x: x['順位']), 
                            key=lambda x: x['性別'])

        # just in case?
        return self.entry_rows
    
    def get_entry_data(self) -> list:
        return self.entry_data        
    

    #=============================================
    #      Data Validataion
    #=============================================

    def check_entry_data(self, studentClass, studentNumber, studentRank) -> str:
        # first just check that the data is of acceptable format
        messages = [
            self._check_format_studentClass(studentClass),
            self._check_format_studentNumber(studentNumber),
            self._check_format_studentRank(studentRank)
        ]
        for msg in messages:
            if msg != '':
                return msg

        # check to see if student is in meibo
        #---- must be checked after the above data is verified
        msg = self._check_student(studentClass, studentNumber)
        if msg != '':
            return msg

        # using this student's rank and gener,
        # check to see if this (gender, rank) combination has been enetered
        #---- must be checked after checking this student exists
        student = self.meibo_lookup(studentClass, studentNumber)
        msg = self._check_gender_rank(student['性別'], studentRank)
        if msg != '':
            return msg

        return ''

    def _check_student(self, studentClass, studentNumber):
        # check if the student is in the meibo
        if not self.meibo_lookup(studentClass, studentNumber):
            return f'「{studentClass} #{studentNumber}」は名簿には入っていないです'

        # check if the student has already been entered
        if self.entry_lookup(studentClass, studentNumber):
            return f'{studentClass} #{studentNumber}は既に入力されました'
        
        return ''

    def _check_gender_rank(self, studentGender, studentRank):
        for entry in self.entry_data:
            if entry['性別'] == studentGender and entry['順位'] == studentRank:
                return f'順位が {studentRank} 番の{studentGender}の生徒は既に入力されました'
            
        return ''

    def _check_format_studentClass(self, studentClass) -> str:
        if studentClass == '':
            return f'組を入れてください'
    
        if not studentClass in self.meibo_classes:
            return f'組：「{studentClass}」 は名簿にはありません'

        return ''

    def _check_format_studentNumber(self, studentNumber) -> str:
        if studentNumber == '':
            return f'出席番号を入れてください'
        
        try:
            int(studentNumber)
        except ValueError:
            return f'番号：「{studentNumber}」 は整数ではありません'
    
        nums = [str(x) for x in range(1,42)]
        if not studentNumber in nums:
            return f'番号：「{studentNumber}」 は範囲外です'

        return ''
       
    def _check_format_studentRank(self, studentRank) -> str:
        if studentRank == '':
            return f'順位を入れてください'
        
        try:
            int(studentRank)
        except ValueError:
            return f'順位：「{studentRank}」 は整数ではありません'

        if not int(studentRank) > 0:
            return f'順位「{studentRank}」 は０より大きくなければなりません'

        return ''
