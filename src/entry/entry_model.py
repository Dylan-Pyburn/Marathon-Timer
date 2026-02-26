
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
        
        self.load_meibo()
        

    def set_meibo_path(self):
        pass

    def load_meibo(self):
        self.meibo_data = defaultdict(dict)

        with open(self.meibo_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                self.meibo_data[row['組']][row['番号']] = {
                    '苗字': row['苗字'],
                    '名前': row['名前'],
                    '性別': row['性別']
                }

    def get_student_info(self, studentClass, studentNumber) -> dict:
        try:
            return self.meibo_data[studentClass][studentNumber]
        except KeyError:
            return None

    def open_records(self):
        pass

    def save_records(self):
        pass

    def saveAs_records(self):
        pass

    #=============================================
    #      Data Validataion
    #=============================================
