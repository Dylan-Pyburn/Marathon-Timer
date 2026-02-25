from tkinter import *
from tkinter import ttk

WINDOW_TITLE    = 'マラソン タイマー'
WINDOW_WIDTH    = 1200
WINDOW_HEIGHT   = 700


class GUI:

    def __init__(self):
        self.configure_gui()

    #=============================================
    #       UI Elements
    #=============================================

    def configure_gui(self):
        self.configure_root()
        self.configure_menubar()
        self.configure_tabControl()
        self.configure_frameTabRankEntry()
        self.configure_frameTabTimer()
        self.configure_frameTabStats()

    def configure_root(self):
        self.root = Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.root.config(bg='white')

    def configure_tabControl(self):
        self.tabControl = ttk.Notebook(self.root)
        self.tabControl.pack(expand=1, fill=BOTH)

    def configure_frameTabRankEntry(self):
        self.frameAppRankEntry = Frame(self.tabControl, bg='skyblue')
        self.frameAppRankEntry.pack(expand=1, fill=BOTH)
        self.tabControl.add(self.frameAppRankEntry, text='順位入力')

        self.configure_frameDataEntry()
        self.configure_frameDataView()

    def configure_frameTabTimer(self):
        self.frameAppTimer = Frame(self.tabControl, bg='#fc8f79')
        self.frameAppTimer.pack(expand=1, fill=BOTH) 
        self.tabControl.add(self.frameAppTimer, text='タイマー')

    def configure_frameTabStats(self):
        self.frameAppStats = Frame(self.tabControl, bg='#073f18')
        self.frameAppStats.pack(expand=1, fill=BOTH)
        self.tabControl.add(self.frameAppStats, text='合計')
    
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

        self.menuFile.add_command(label='新規',             command=None)
        self.menuFile.add_command(label='開く',             command=None)
        self.menuFile.add_command(label='エクスポート',     command=None)
        self.menuFile.add_command(label='保存',             command=None)
        self.menuFile.add_command(label='名前を付けて保存', command=None)
        self.menuFile.add_separator()
        self.menuFile.add_command(label='閉じる',           command=None)

    def configure_menuSettings(self):
        self.menuSettings = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='設定', menu=self.menuSettings)

        self.menuSettings.add_command(label='言語',         command=None)
        self.menuSettings.add_command(label='キーマップ',   command=None)

    def configure_menuHelp(self):
        self.menuHelp = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='ヘルプ', menu=self.menuHelp)

        self.menuHelp.add_command(label='使い方',           command=None)
        self.menuHelp.add_command(label='Docs',             command=None)

    #== Tabs ===== =============================== 

    #== Data Entry =============================== 

    def configure_frameDataEntry(self):
        self.frameDataEntry = Frame(self.frameAppRankEntry, width=500, height=150,bg="white")

        self.labelStudentClass      = Label(self.frameDataEntry, text='組')
        self.entryStudentClass      = Entry(self.frameDataEntry)

        self.labelStudentNumber     = Label(self.frameDataEntry, text='出席番号')
        self.entryStudentNumber     = Entry(self.frameDataEntry)
        
        self.labelStudentRank       = Label(self.frameDataEntry, text='順位')
        self.entryStudentRank       = Entry(self.frameDataEntry)

        self.buttonEnterData        = Button(self.frameDataEntry, text='追加', command=self.action_buttonEnterData)

        self.arrange_frameDataEntry()

    def arrange_frameDataEntry(self):
        self.labelStudentClass.grid(    row=0,  column=0,   padx=10,    pady=10)
        self.entryStudentClass.grid(    row=1,  column=0,   padx=10,    pady=10)

        self.labelStudentNumber.grid(   row=0,  column=1,   padx=10,    pady=10)
        self.entryStudentNumber.grid(   row=1,  column=1,   padx=10,    pady=10)

        self.labelStudentRank.grid(     row=0,  column=2,   padx=10,    pady=10)
        self.entryStudentRank.grid(     row=1,  column=2,   padx=10,    pady=10)

        self.buttonEnterData.grid(      row=1,  column=3,   padx=20,    pady=10)

        self.frameDataEntry.pack(side='top', anchor="center", pady= 20)

    #== Data View ================================ 

    def configure_frameDataView(self):
        self.frameDataView = Frame(self.frameAppRankEntry, width=500, height=100, bg="white")
        self.frameDataView.pack(side='top', anchor='center', pady=20)
        
        self.listboxDataView = Listbox(self.frameDataView)
        self.listboxDataView.pack(side=LEFT, fill=BOTH)

        self.scrollbarDataView = Scrollbar(self.frameDataView, command=self.listboxDataView.yview)
        self.scrollbarDataView.pack(side=RIGHT, fill=BOTH)
        
        self.listboxDataView.config(yscrollcommand = self.scrollbarDataView.set)


    #=============================================
    #       Commands
    #=============================================

    def action_buttonEnterData(self):
        self.listboxDataView.insert(END,'hi')


