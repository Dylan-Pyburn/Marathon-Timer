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
            self.view.var_dataViewRadio.set('meibo')
            self._update_listboxDataView()
            self._show_label_message(label, path)
            
        else:
            self._show_label_error(label, msg)



    def choose_entry_file(self):
        '''
        Handle the choosing of a new file or loading an existing one
        '''
        pass


    def add_entry(self):
        label = self.view.labelMessage
        self._reset_label(label)
        
        studentClass    = self.view.var_studentClass.get().strip().upper()
        studentNumber   = self.view.var_studentNumber.get().strip().upper()
        studentRank     = self.view.var_studentRank.get().strip().upper()
        
        errorMessage    = self.model.check_entry_data(studentClass, studentNumber, studentRank)
        
        if errorMessage != '':
            self._show_label_error(label, errorMessage)
           
        else:
            self.model.add_entry(studentClass, studentNumber, studentRank)

            self.view.var_dataViewRadio.set('entry')
            self._update_listboxDataView()
            self._reset_entryvars()


    def save_entries(self):
        #TODO get path to save if not set?

        self.model.save_entries()

    def handle_display_radio(self):
        self._update_listboxDataView()

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

    def _update_listboxDataView(self):
        mode = self.view.var_dataViewRadio.get()

        if mode == 'meibo':
            self._show_listbox_meibo()
        elif mode == 'entry':
            self._show_listbox_entries()
        
    def _show_listbox_meibo(self):
        self.view.listboxDataView.delete(0, 'end')
        
        data = self.model.get_meibo_rows()
        for line in data:
            self.view.listboxDataView.insert('end', line)

    def _show_listbox_entries(self):
        self.view.listboxDataView.delete(0, 'end')

        data = self.model.get_entry_rows()
        for line in reversed(data):
            self.view.listboxDataView.insert('end', line)

    
