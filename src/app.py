import  tkinter as      tk
from    tkinter import  ttk

from src.entry.entry_view       import EntryView
from src.entry.entry_controller import EntryController

'''
TODO
    entryview
        data extry
            entered items are valid
                move to model?
            student can be found in meibo
            show error label
        read from meibo:
            class combobox
            number combobox
        combobox autocomplete
        lbDataView
            get more data from meibo (gender, name)
            edit and entry (repeat data validation)

    entry model and controller
        read from meibo to populate inital value
        read from meibo to populate name and gender
        write to csv
    
    add menu
    add tabs

    timer
    stats
'''

WINDOW_TITLE    = 'マラソン タイマー'
WINDOW_WIDTH    = 1200
WINDOW_HEIGHT   = 700

class App(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.title(WINDOW_TITLE)
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        #self.config(bg='white')

        self.entryFrame         = EntryView(self)
        self.entryController    = EntryController(self.entryFrame)

        self.entryFrame.set_controller(self.entryController)
        self.entryFrame.grid(row=0, column=0, padx=20, pady=20)

        self.bind('<Return>', self.entryFrame.pressed_enter)

    def start(self):
        self.mainloop()
