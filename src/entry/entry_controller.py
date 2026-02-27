import  tkinter as      tk
from    tkinter import  filedialog as fd


class EntryController:

    def __init__(self, view, model):
        self.view   = view
        self.model  = model

    #=============================================
    #      Handle Commands
    #=============================================

    def choose_meibo_file(self) -> None:
        '''
        create a dialog for the user to chooose a meibo csv

        if chosen, set the meibo path and attempt to load it
            if success:
                display the meibo data in the listbox
            if  fails: 
                display error dialog
        '''
        label = self.view.labelMeiboPath
        self._reset_label(label)

        path = self._open_file_dialog('名簿')

        # cancel button clicked, nothing chosen
        if len(path) == 0:
            return
        
        # make sure a CSV was chosen
        if path.split('.')[-1] != 'csv':
            self._show_label_error(label, 'choose a CSV file')

        # try loading the CSV
        self.model.set_meibo_path(path)
        msg = self.model.load_meibo()        

        if msg == '':
            self._show_label_message(label, path)
            '''TODO: show meibo in listbox if radio is configured'''
        else:
            self._show_label_error(label, msg)


    def choose_entry_file(self):
        '''
        Handle the choosing of a new file or loading an existing one
        '''
        pass


    def add_entry(self):
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
            self._reset_entry_vars()


    def save_entries(self):
        #TODO get path to save if not set?

        self.model.save_entries()

    #=============================================
    #      Dialogs, UI Updates
    #=============================================

    def _open_file_dialog(self, title:str, initialdir:str='.') -> str:
        filetypes = (('CSV ファイル', '*.csv'), ('全部', '*.*'))
        
        path = fd.askopenfilename(
            title       = title,
            initialdir  = initialdir,
            filetypes   = filetypes 
        )
        return path

    def _show_label_message(self, label:tk.Label, message:str) -> None:
        label.config(text=message, fg='black')

    def _show_label_error(self, label:tk.Label, message:str) -> None:
        label.config(text=message, fg='red')

    def _reset_label(self, label:tk.Label) -> None:
        self._show_label_message(label, '')

    def _reset_entryvars(self) -> None:
        self.view.var_studentClass.set('')
        self.view.var_studentNumber.set('')
        self.view.var_studentRank.set('')

