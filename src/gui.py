from tkinter import *

WINDOW_TITLE    = 'マラソン タイマー'
WINDOW_WIDTH    = 1200
WINDOW_HEIGHT   = 700


class GUI:

    def __init__(self):
        self.configure_gui()

    #=============================================
    #       Widgets
    #=============================================

    def configure_gui(self):
        self.configure_root()
        self.configure_menubar()
        self.configure_frameDataEntry()
        self.configure_frameDataView()
        
    def configure_root(self):
        self.root = Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.root.config(bg='skyblue')
    
    #== Menu ===================================== 
    
    def configure_menubar(self):
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        self.configure_menuFile()
        self.configure_menuSettings()
        self.configure_menuHelp()

    def configure_menuFile(self):
        self.menuFile = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='ファイル', menu=self.menuFile)

        self.menuFile.add_command(label='新規', command=None)
        self.menuFile.add_command(label='開く', command=None)
        self.menuFile.add_separator()
        self.menuFile.add_command(label='保存', command=None)
        self.menuFile.add_command(label='名前を付けて保存', command=None)

    def configure_menuSettings(self):
        self.menuSettings = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='設定', menu=self.menuSettings)

        self.menuSettings.add_command(label='言語', command=None)
        self.menuSettings.add_command(label='キーマップ', command=None)

    def configure_menuHelp(self):
        self.menuHelp = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='ヘルプ', menu=self.menuHelp)

        self.menuHelp.add_command(label='使い方', command=None)
        self.menuHelp.add_command(label='Docs', command=None)

    #== Data Entry =============================== 

    def configure_frameDataEntry(self):
        self.frameDataEntry = Frame(self.root, width=700, height=150,bg="white")
        self.frameDataEntry.pack(side='top', anchor="center", pady= 20)

    def configure_frameDataView(self):
        self.frameDataView = Frame(self.root, width=700, height=300, bg="white")
        self.frameDataView.pack(side='top', anchor='center', pady=20)


    #=============================================
    #       Commands
    #=============================================


