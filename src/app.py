import  tkinter as      tk
from    tkinter import  ttk

from src.entry.entry_view import EntryView

'''
TODO
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

        self.entryFrame = EntryView(self)
        self.entryFrame.grid(row=0, column=0, padx=20, pady=20)


    def start(self):
        self.mainloop()
