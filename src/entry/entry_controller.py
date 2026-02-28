import  tkinter as      tk
from    tkinter import  filedialog as fd

from src.entry.entry_model import EntryModel

RADIO_VIEW_MODES = ['meibo', 'entry']
RADIO_SORT_MODES = ['newest', 'oldest', 'sortedMale', 'sortedFemale']

FILETYPES =  [('CSV ファイル', '*.csv')]

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
            self._update_listboxDataView(viewmode='meibo')
            self._show_label_message(label, path)
            
        else:
            self._show_label_error(label, msg)


    def choose_entry_file(self):
        '''
        Handle the choosing of a new file or loading an existing one
        '''
        label = self.view.labelEntryPath
        self._reset_label(label)

        path = self._save_as_dialog('結果ファイル')
        print(f'"{path}"')

        # check that something was chosen
        if len(path) == 0:
            return

        # make sure it's non-empty and is csv
        if path.split('.')[-1] != 'csv':
            self._show_label_error(label, 'choose a CSV file')
        else:
            self.model.set_entries_path(path)
            self._show_label_message(label, path)


    def add_entry(self):
        label = self.view.labelMessage
        self._reset_label(label)
        
        studentClass    = self.view.var_studentClass.get().strip().upper()
        studentNumber   = self.view.var_studentNumber.get().strip().upper()
        studentRank     = self.view.var_studentRank.get().strip().upper()
        
        errorMessage    = self.model.check_entry_data(studentClass, studentNumber, studentRank)
        
        if errorMessage != '':
            self._show_label_error(label, errorMessage)
            return
    
        self.model.add_entry(studentClass, studentNumber, studentRank)
        self._update_listboxDataView(viewmode='entry')
        
        # because its nicer for the user:
        self._reset_entryvars()
        self.view.entryStudentClass.focus_set()


    def save_entries(self):
        self._update_listboxDataView(viewmode='entry')
        label = self.view.labelMessage
        
        if len(self.model.get_entry_rows()) == 0:
            self._show_label_message(label, 'there are no entries to write')
            return

        # choose a file to save to if not already set
        if self.model.get_entries_path() == '':
            self.choose_entry_file()

        msg = self.model.save_entries()
        if msg == '':
            self._show_label_message(label, f'Entries saved')
        else:
            self._show_label_error(label, msg)


    def handle_radio_display(self):
        self._update_listboxDataView()

    def handle_radio_sort(self):
        if self.view.var_radioDataView.get() != 'entry':
            return
        self._update_listboxDataView()

    def handle_checkbutton_sort(self):
        if self.view.var_radioDataView.get() != 'entry':
            return
        self._update_listboxDataView()

    #=============================================
    #      Dialogs, UI Updates
    #=============================================

    def _update_listboxDataView(self, viewmode:str='', sortmode=''):
        # set a new viewmode if provided otherwise use the current one
        if viewmode in RADIO_VIEW_MODES:
            self.view.var_radioDataView.set(viewmode)
        else:
            viewmode = self.view.var_radioDataView.get()

        # set a new sortmode if provided otherwise use the current one
        if sortmode in RADIO_SORT_MODES:
            self.view.var_radioDataSort.set(sortmode)
        else:
            sortmode = self.view.var_radioDataSort.get()

        if viewmode == 'meibo':
            self._show_listbox_meibo()
        elif viewmode == 'entry':
            self._show_listbox_entries()
        
    def _show_listbox_meibo(self):
        self.view.listboxDataView.delete(0, 'end')
        
        data = self.model.get_meibo_rows()
        for line in data:
            self.view.listboxDataView.insert('end', line)

    def _show_listbox_entries(self):
        self.view.listboxDataView.delete(0, 'end')
        
        sortmode    = self.view.var_radioDataSort.get()
        data        = self.model.get_entries(sortmode)

        # only show selected genders
        selectedGenders = []
        if self.view.var_checkboxMale.get():    selectedGenders.append('男子')
        if self.view.var_checkboxFemale.get():  selectedGenders.append('女子')

        # filter out unselected genders
        data = [line for line in data if line['性別'] in selectedGenders]
        for line in data:
            entrystr = EntryModel.get_entry_str(line)
            self.view.listboxDataView.insert('end', entrystr)

    def _open_file_dialog(self, title:str, initialdir:str='.') -> str:     
        path = fd.askopenfilename(
            title       = title,
            initialdir  = initialdir,
            filetypes   = FILETYPES
        )
        return path
    
    def _save_as_dialog(self, title:str, initialdir:str='.') -> str:
        path = fd.asksaveasfilename(
            title               = title,
            initialdir          = initialdir,
            defaultextension    = '.csv',
            filetypes           = FILETYPES
        )
        return path

    def _show_label_message(self, label:tk.Label, message:str) -> None:
        label.config(text=message)

    def _show_label_error(self, label:tk.Label, message:str) -> None:
        label.config(text=message)

    def _reset_label(self, label:tk.Label) -> None:
        self._show_label_message(label, '')

    def _reset_entryvars(self) -> None:
        self.view.var_studentClass.set('')
        self.view.var_studentNumber.set('')
        self.view.var_studentRank.set('')

    
