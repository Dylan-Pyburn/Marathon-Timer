
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
        
        self.entry_data = []

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

    def open_records(self):
        pass

    def save_records(self):
        pass

    def saveAs_records(self):
        pass

    #=============================================
    #      Data Processing
    #=============================================

    def get_student_info(self, studentClass:str, studentNumber:str) -> dict:
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

    def add_entry(self, studentClass, studentNumber, studentRank) -> bool:
        studentInfo = self.get_student_info(studentClass, studentNumber)

        if studenInfo == None:
            return False

        studentFamilyName   = studentInfo['苗字']
        studentFirstName    = studentInfo['名前']
        studentGender       = studentInfo['性別']

        self.entry_data.append({
            '順位'  : studentRank,
            '組'    : studentClass,
            '番号'  : StudentNumber,
            '性別'  : studentGender,
            '苗字'  : studentFamilyName,
            '名前'  : studentFirstName
        })



    #=============================================
    #      Data Validataion
    #=============================================