import src.entry.entry_model as em

class EntryController:

    def __init__(self, view, model):
        self.view   = view
        self.model  = model

    def clicked_saveButton(self):
        self._reset_labelMessage()
        
        studentClass    = self.view.var_studentClass.get().strip().upper()
        studentNumber   = self.view.var_studentNumber.get().strip().upper()
        studentRank     = self.view.var_studentRank.get().strip().upper()
        
        if self._check_data(studentClass, studentNumber, studentRank):
            
            newEntry = self.model.add_entry(studentClass, studentNumber, studentRank)

            entry = f'{newEntry['性別']}{newEntry['順位']}  {newEntry['組']}  #{newEntry['番号']}  {newEntry['苗字']} {newEntry['名前']}'


            self.view.listboxDataView.insert('1', entry)
            self._reset_vars()


    def _reset_labelMessage(self):
        self.view.labelMessage.config(text='')

    def _reset_vars(self):
        self.view.var_studentClass.set('')
        self.view.var_studentNumber.set('')
        self.view.var_studentRank.set('')


    #=============================================
    #      Data Validataion
    #=============================================
    
    def _check_data(self, studentClass, studentNumber, studentRank) -> bool:
        return all([
            self._check_studentRank(studentRank),
            self._check_studentNumber(studentNumber),
            self._check_studentClass(studentClass)
        ])
    
    def _check_studentClass(self, studentClass):
        if studentClass == '':
            self.view.labelMessage.config(text=f'組を入れてください')
            return False 
    
        if not studentClass in em.CLASSES:
            self.view.labelMessage.config(text=f'組：「{studentClass}」 は組ではありません')
            return False

        return True
    
    def _check_studentNumber(self, studentNumber):
        if studentNumber == '':
            self.view.labelMessage.config(text=f'出席番号を入れてください')
            return False 

        try:
            int(studentNumber)
        except ValueError:
            self.view.labelMessage.config(text=f'番号：「{studentNumber}」 は整数ではありません')
            return False 
    
        nums = [str(x) for x in range(1,42)]
        if not studentNumber in nums:
            self.view.labelMessage.config(text=f'番号：「{studentNumber}」 は範囲外です')
            return False

        return True 

    def _check_studentRank(self, studentRank):
        if studentRank == '':
            self.view.labelMessage.config(text=f'順位を入れてください')
            return False 
        
        try:
            int(studentRank)
        except ValueError:
            self.view.labelMessage.config(text=f'順位：「{studentRank}」 は整数ではありません')
            return False 

        if not int(studentRank) > 0:
            self.view.labelMessage.config(text=f'順位「{studentRank}」 は０より大きくなければなりません')
            return False

        return True