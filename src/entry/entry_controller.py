
class EntryController:

    def __init__(self, view):
        self.view = view

    def clicked_saveButton(self):
        studentClass    = self.view.var_studentClass.get()
        studentNumber   = self.view.var_studentNumber.get()
        studentRank     = self.view.var_studentRank.get()
        
        print(studentClass, studentNumber, studentRank)
        