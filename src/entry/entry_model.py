
from collections import defaultdict
import csv

MEIBO_FIELDS = ['組','番号','性別','苗字','名前']
ENTRY_FIELDS = ['順位','組','番号','性別','苗字','名前']

class EntryModel:

    def __init__(self):
        self.meibo_path     = ''
        self.entries_path   = ''
        
        self.meibo_data = defaultdict(dict)
        self.entry_data = []

        self.meibo_classes = []
    
    #=============================================
    #      File Operations
    #=============================================        

    def set_meibo_path(self, path:str) -> bool:
        self.meibo_path = path
        
    def get_meibo_path(self) -> str:
        return self.meibo_path

    def load_meibo(self) -> str:
        # read meibo file
        try:
            rows = []
            with open(self.meibo_path, mode='r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                fieldnames = csv_reader.fieldnames
                for row in csv_reader:
                    rows.append(row)
        except:
            return f'error while opening{self.meibo_path}'

        # check the meibo data
        msg = self.check_meibo_file_format(fieldnames, rows)
        if msg != '':
            return msg

        # everything looks good, parse the data
        meibo_data = defaultdict(dict)
        for row in rows:
            self.meibo_data[row['組']][row['番号']] = {
                '苗字': row['苗字'],
                '名前': row['名前'],
                '性別': row['性別']
            }
        self.meibo_classes  = [k for k in self.meibo_data.keys()]
        self.meibo_data     = meibo_data

        return ''

    
    def get_entries_path(self) -> str:
        return self.entries_path

    
    def set_entries_path(self, path:str) -> None:
        self.entries_path = path
    

    def save_entries(self):
        if len(self.entry_data) == 0:
            return

        with open(self.entries_path, mode='w', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=ENTRY_FIELDS)

            csv_writer.writeheader()
            csv_writer.writerows(self.entry_data)


    #=============================================
    #      Data Processing
    #=============================================

    def meibo_lookup(self, studentClass:str, studentNumber:str) -> dict:
        '''
        組と出席番号を使い、ある生徒の苗字、名前、性別を調べる

        Params:
            (str) studentClass  :  組
            (str) studentNumber :  出席番号
        Return:
            ある: dict{苗字, 名前, 性別}
            ない: None
        '''
        try:
            return self.meibo_data[studentClass][studentNumber]
        except KeyError:
            return None

    def add_entry(self, studentClass, studentNumber, studentRank):
        studentInfo = self.meibo_lookup(studentClass, studentNumber)

        if studentInfo == None:
            return None

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

        self.entry_data.append(newEntry)
        return newEntry

    def get_entry_str(self, entry:dict) -> str:
        return f'{entry['性別']}{entry['順位']}  {entry['組']}  #{entry['番号']}  {entry['苗字']} {entry['名前']}'

    def get_student_classes(self):
        return self.meibo_classes

    def get_numbers(self, studentClass):
        pass

    #=============================================
    #      Data Validataion
    #=============================================

    def check_meibo_file_format(self, fieldnames:list, rows:dict) -> str:
        
        # the meibo may have other fields, but the expected ones must be included
        for field in MEIBO_FIELDS:
            if not field in fieldnames:
                return f'{field} must be in CSV fields'
            
        # make sure that all the data is there for every row
        for row in rows:
            for field in MEIBO_FIELDS:
                if row[field] == None:
                    return f'atleast one row was missing data'
        
        return ''

    def check_entry_data(self, studentClass, studentNumber, studentRank) -> str:
        messages = [
            self._check_studentClass(studentClass),
            self._check_studentNumber(studentNumber),
            self._check_studentRank(studentRank)
        ]
        for msg in messages:
            if msg != '':
                return msg

        # must be checked after because can only be checked with valid data
        msg = self._check_student(studentClass, studentNumber)
        if msg != '':
            return msg
        
        return ''

    def _check_student(self, studentClass, studentNumber):
        # check if the student is in the meibo
        if not self.meibo_lookup(studentClass, studentNumber):
            return f'「{studentClass} #{studentNumber}」は名簿には入っていないです'

        # check if the student has already been entered
        for entry in self.entry_data:
            if entry['組'] == studentClass and entry['番号'] == studentNumber:
                return f'{studentClass} #{studentNumber}」は既に入れらました'
        
        return ''


    def _check_studentClass(self, studentClass) -> str:
        if studentClass == '':
            return f'組を入れてください'
    
        if not studentClass in self.meibo_classes:
            return f'組：「{studentClass}」 は名簿にはありません'

        return ''

   
    def _check_studentNumber(self, studentNumber) -> str:
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
       

    def _check_studentRank(self, studentRank) -> str:
        if studentRank == '':
            return f'順位を入れてください'
        
        try:
            int(studentRank)
        except ValueError:
            return f'順位：「{studentRank}」 は整数ではありません'

        if not int(studentRank) > 0:
            return f'順位「{studentRank}」 は０より大きくなければなりません'

        return ''
