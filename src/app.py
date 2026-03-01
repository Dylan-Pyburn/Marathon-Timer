import  tkinter         as  tk
#import  ttkbootstrap    as  ttk
import customtkinter    as ctk

from src.entry.entry_view       import EntryView
from src.entry.entry_model      import EntryModel
from src.entry.entry_controller import EntryController

'''
TODO
    entryview
        read from meibo:
            cant load new meibo once something has been entered(disable button)
            class combobox
            number combobox
        combobox autocomplete
    
    entry file
    open file: for editing
        but how to verify that an okay meibo?
            must choose a meibo if not chosen already
            then all entries must pass  meibo_lookup

    check that a loaded entry file has a correct meibo
    
    data entry
        edit an entry from the listbox
        display entries in forward or reverse order or sorted (have buttons that are only visible on entry mode)
        can edit listbox lines, but only for entry mode
        can delete listbox lines, but only for entry mode

        loading
            load entries file
        

    styling
        make it look purdy
        auto hide/show scrollbar
        autofill entries
        entries combobox

    make displayed file loacation clickable?
        
    ask to save on program exit

    add tabs

    timer
    stats
'''


WINDOW_TITLE    = 'マラソン タイマー'
WINDOW_WIDTH    = 900
WINDOW_HEIGHT   = 650

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        ctk.set_default_color_theme('themes/theme.json')


        self.title(WINDOW_TITLE)
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.minsize(800, 650)


        self.entryFrame         = EntryView(self)
        self.entryModel         = EntryModel()
        self.entryController    = EntryController(self.entryFrame, self.entryModel)

        self.entryFrame.set_controller(self.entryController)
        self.entryFrame.pack(expand=True, fill=tk.BOTH)

        self.bind('<Return>', self.entryFrame.pressed_enter)

    def start(self):
        self.mainloop()
