
from collections import defaultdict
import csv

CLASSES = [
    'M11', 'M12', 'E11', 'E12', 'B1', 'C1',
    'M21', 'M22', 'E21', 'E32', 'B2', 'C2',
    'M31', 'M32', 'E31', 'E32', 'B3', 'C3'
]

class EntryModel:

    def __init__(self):
        self.meibo_path = 'meibo.csv'
        
        self.meibo_data = {}
        self.entry_data = []

        self.meibo_classes = []

        self.load_meibo()

        
    
    #=============================================
    #      File Operations
    #=============================================        

    def set_meibo_path(self, path:str) -> None:
        self.meibo_path = path
        
    def get_meibo_path(self) -> str:
        return self.meibo_path

    def load_meibo(self) -> None:
        self.meibo_data = defaultdict(dict)

        with open(self.meibo_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                self.meibo_data[row['組']][row['番号']] = {
                    '苗字': row['苗字'],
                    '名前': row['名前'],
                    '性別': row['性別']
                }
        
        self.meibo_classes = [k for k in self.meibo_data.keys()]

    def open_records(self):
        pass

    def save_records(self):
        pass

    def saveAs_records(self):
        pass

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

        self.entry_data.append({
            '順位'  : studentRank,
            '組'    : studentClass,
            '番号'  : studentNumber,
            '性別'  : studentGender,
            '苗字'  : studentFamilyName,
            '名前'  : studentFirstName
        })

        return self.entry_data[-1]

    def get_student_classes(self):
        return self.meibo_classes

    def get_numbers(self, studentClass):
        pass

    #=============================================
    #      Data Validataion
    #=============================================

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
