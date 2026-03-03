import  tkinter         as tk
import  customtkinter   as ctk
from    tkinter import  filedialog  as fd

from src.entry.entry_model import EntryModel

RADIO_VIEW_MODES = ['meibo', 'entry']
RADIO_SORT_MODES = ['newest', 'oldest', 'sortedMale', 'sortedFemale']

FILETYPES =  [('CSV ファイル', '*.csv')]

class EntryController:

    def __init__(self, view, model):
        self.view   = view
        self.model  = model

        self.switch_app_theme()

    #=============================================
    #      Handle Commands
    #=============================================

    def switch_app_theme(self):
        darkmode = self.view.switchAppTheme.get()
        ctk.set_appearance_mode( 'dark' if darkmode else 'light' )


    def choose_meibo_file(self) -> None:
        '''
        create a dialog for the user to chooose a meibo csv

        if chosen, set the meibo path and attempt to load it
            if success:
                display the meibo data in the listbox
            if  fails: 
                display error dialog

        TODO
        handle Meibo exceptions
        file not found error

        '''
        label = self.view.labelMeiboPath

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

    def choose_time_data_file(self):
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
            return
    
        self.model.add_entry(studentClass, studentNumber, studentRank)
        self._update_scrollFrameDataDisplay(viewmode='entry')
        
        # because its nicer for the user:
        self._reset_entryvars()
        self.view.entryStudentClass.focus_set()

    def remove_entry(self, buttonNum):
        self.view.scrollFrameDataView.get_item(buttonNum)
        self.view.scrollFrameDataView.remove_item(buttonNum)


    def save_entries(self):
        self._update_scrollFrameDataDisplay(viewmode='entry')
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
        self._update_scrollFrameDataDisplay()

    def handle_radio_sort(self):
        if self.view.var_radioDataView.get() != 'entry':
            return
        self._update_scrollFrameDataDisplay()

    def handle_checkbutton_sort(self):
        if self.view.var_radioDataView.get() != 'entry':
            return
        self._update_scrollFrameDataDisplay()

    #=============================================
    #      Dialogs, UI Updates
    #=============================================

    def _update_scrollFrameDataDisplay(self,  viewmode:str='', sortmode=''):
        # set a new viewmode if provided
        if viewmode in RADIO_VIEW_MODES:
            self.view.var_radioDataView.set(viewmode)
    
        # set a new sortmode if provided
        if sortmode in RADIO_SORT_MODES:
            self.view.var_radioDataSort.set(sortmode)
       
        viewmode = self.view.var_radioDataView.get()
        sortmode = self.view.var_radioDataSort.get()

        self.view.scrollFrameDataView.clear()
        if viewmode == 'meibo':
            self._show_data_meibo()
        elif viewmode == 'entry':
            self._show_data_entries()
        

    def _show_data_meibo(self):
        data = self.model.get_meibo_rows()
        for line in data:
            self.view.scrollFrameDataView.add_item(line, showDelBtn=False)


    def _show_data_entries(self):
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
            self.view.scrollFrameDataView.add_item(entrystr)

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
        label.configure(text=message)

    def _show_label_error(self, label:tk.Label, message:str) -> None:
        label.configure(text=message)

    def _reset_label(self, label:tk.Label) -> None:
        self._show_label_message(label, '')

    def _reset_entryvars(self) -> None:
        self.view.var_studentClass.set('')
        self.view.var_studentNumber.set('')
        self.view.var_studentRank.set('')

    
