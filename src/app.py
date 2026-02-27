import  tkinter as      tk
from    tkinter import  ttk

from src.entry.entry_view       import EntryView
from src.entry.entry_model      import EntryModel
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
            error checking to verify format/integrity of csv data
            cant load new meibo once something has been entered(disable button)
            class combobox
            number combobox
        combobox autocomplete
        lbDataView
            get more data from meibo (gender, name)
            edit and entry (repeat data validation)

    TODO
    filedialog
        add all fire dialog operations
        load entries into listbox
    data entry
        edit an entry from the listbox
    styling
        make it look purdy
        auto hide/show scrollbar
        autofill entries
        entries combobox

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
WINDOW_WIDTH    = 700
WINDOW_HEIGHT   = 700

class App(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.title(WINDOW_TITLE)
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        #self.config(bg='white')

        #self.configure_menubar()

        self.entryFrame         = EntryView(self)
        self.entryModel         = EntryModel()
        self.entryController    = EntryController(self.entryFrame, self.entryModel)

        self.entryFrame.set_controller(self.entryController)
        self.entryFrame.grid(row=0, column=0, padx=20, pady=20)

        self.bind('<Return>', self.entryFrame.pressed_enter)

    def start(self):
        self.mainloop()



    '''
    def configure_menubar(self):
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        self.configure_menuFile()
        self.configure_menuSettings()
        self.configure_menuHelp()

    def configure_menuFile(self):
        self.menuFile = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='ファイル', menu=self.menuFile)

        self.menuFile.add_command(label='新規',             command=None)
        self.menuFile.add_command(label='開く',             command=None)
        self.menuFile.add_command(label='エクスポート',     command=None)
        self.menuFile.add_command(label='保存',             command=None)
        self.menuFile.add_command(label='名前を付けて保存', command=None)
        self.menuFile.add_separator()
        self.menuFile.add_command(label='閉じる',           command=None)

    def configure_menuSettings(self):
        self.menuSettings = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='設定', menu=self.menuSettings)

        self.menuSettings.add_command(label='言語',         command=None)
        self.menuSettings.add_command(label='キーマップ',   command=None)

    def configure_menuHelp(self):
        self.menuHelp = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='ヘルプ', menu=self.menuHelp)

        self.menuHelp.add_command(label='使い方',           command=None)
        self.menuHelp.add_command(label='Docs',             command=None)
    '''