
from collections import defaultdict
import csv

CLASSES = [
    'M11', 'M12', 'E11', 'E12', 'B1', 'C1',
    'M21', 'M22', 'E21', 'E32', 'B2', 'C2',
    'M31', 'M32', 'E31', 'E32', 'B3', 'C3'
]

class EntryModel:

    def __init__(self):
        self.meibo_path = None
        self.save_path = None

    def set_meibo_path(self):
        pass

    def load_meibo(self):
        pass

    def open_records(self):
        pass

    def save_records(self):
        pass

    def saveAs_records(self):
        pass

    #=============================================
    #      Data Validataion
    #=============================================

