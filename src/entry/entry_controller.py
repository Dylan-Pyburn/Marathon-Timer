from tkinter import filedialog as fd

'''
https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/
'''

class EntryController:

    def __init__(self, view, model):
        self.view   = view
        self.model  = model

    def clicked_add_entry(self):
        self._reset_labelMessage()
        
        studentClass    = self.view.var_studentClass.get().strip().upper()
        studentNumber   = self.view.var_studentNumber.get().strip().upper()
        studentRank     = self.view.var_studentRank.get().strip().upper()
        
        errorMessage    = self.model.check_entry_data(studentClass, studentNumber, studentRank)
        
        if errorMessage != '':
            self.view.labelMessage.config(text=errorMessage)
           
        else:
            newEntry    = self.model.add_entry(studentClass, studentNumber, studentRank)
            entryText   = f'{newEntry['性別']}{newEntry['順位']}  {newEntry['組']}  #{newEntry['番号']}  {newEntry['苗字']} {newEntry['名前']}'
            self.view.listboxDataView.insert('1', entryText)
            self._reset_vars()

    def clicked_save_entries(self):
        #TODO get path to save if not set?

        self.model.save_entries()


    def _reset_labelMessage(self):
        self.view.labelMessage.config(text='')

    def _reset_vars(self):
        self.view.var_studentClass.set('')
        self.view.var_studentNumber.set('')
        self.view.var_studentRank.set('')

