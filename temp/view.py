from tkinter import *
from tkinter import ttk

WINDOW_TITLE    = 'マラソン タイマー'
WINDOW_WIDTH    = 1200
WINDOW_HEIGHT   = 700


class View:

    def __init__(self):
        self.configure_root()
        
        self.var_studentClass   = StringVar(self.root)
        self.var_studentNumber  = StringVar(self.root)
        self.var_studentRank    = StringVar(self.root)
        
        self.configure_gui()

    #=============================================
    #      Main UI Elements
    #=============================================

    def configure_gui(self):
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

        self.menuFile.add_command(label='新規',             command=self.cmd_menuFile_new)
        self.menuFile.add_command(label='開く',             command=self.cmd_menuFile_open)
        self.menuFile.add_command(label='エクスポート',     command=self.cmd_menuFile_export)
        self.menuFile.add_command(label='保存',             command=self.cmd_menuFile_save)
        self.menuFile.add_command(label='名前を付けて保存', command=self.cmd_menuFile_saveAs)
        self.menuFile.add_separator()
        self.menuFile.add_command(label='閉じる',           command=self.cmd_menuFile_close)

    def configure_menuSettings(self):
        self.menuSettings = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='設定', menu=self.menuSettings)

        self.menuSettings.add_command(label='言語',         command=self.cmd_menuSettings_language)
        self.menuSettings.add_command(label='キーマップ',   command=self.cmd_menuSettings_keymap)

    def configure_menuHelp(self):
        self.menuHelp = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='ヘルプ', menu=self.menuHelp)

        self.menuHelp.add_command(label='使い方',           command=self.cmd_menuHelp_howToUse)
        self.menuHelp.add_command(label='Docs',             command=self.cmd_menuHelp_docs)

    #=============================================
    #      Rank Entry Tab
    #=============================================

    def configure_frameTabRankEntry(self):
        self.frameAppRankEntry = Frame(self.tabControl, bg='skyblue')
        self.frameAppRankEntry.pack(expand=1, fill=BOTH)
        self.tabControl.add(self.frameAppRankEntry, text='順位入力')

        self.configure_frameDataEntry()
        self.configure_frameDataView()

    #== Data Entry =============================== 

    def configure_frameDataEntry(self):
        self.frameDataEntry = Frame(self.frameAppRankEntry, width=500, height=150,bg="white")

        self.labelStudentClass      = Label(self.frameDataEntry, text='組')
        self.entryStudentClass      = Entry(self.frameDataEntry, textvariable=self.var_studentClass)

        self.labelStudentNumber     = Label(self.frameDataEntry, text='出席番号')
        self.entryStudentNumber     = Entry(self.frameDataEntry, textvariable=self.var_studentNumber)
        
        self.labelStudentRank       = Label(self.frameDataEntry, text='順位')
        self.entryStudentRank       = Entry(self.frameDataEntry, textvariable=self.var_studentRank)

        self.buttonSaveChange       = Button(self.frameDataEntry, text='保存', command=self.cmd_buttonSaveChange, state=NORMAL)
        self.buttonEnterData        = Button(self.frameDataEntry, text='追加', command=self.cmd_buttonEnterData)

        self.arrange_frameDataEntry()

    def arrange_frameDataEntry(self):
        self.labelStudentClass.grid(    row=0,  column=0,   padx=10,    pady=10)
        self.entryStudentClass.grid(    row=1,  column=0,   padx=10,    pady=10)

        self.labelStudentNumber.grid(   row=0,  column=1,   padx=10,    pady=10)
        self.entryStudentNumber.grid(   row=1,  column=1,   padx=10,    pady=10)

        self.labelStudentRank.grid(     row=0,  column=2,   padx=10,    pady=10)
        self.entryStudentRank.grid(     row=1,  column=2,   padx=10,    pady=10)

        self.buttonSaveChange.grid(     row=0,  column=3,   padx=20,    pady=10)
        self.buttonEnterData.grid(      row=1,  column=3,   padx=20,    pady=10)

        self.frameDataEntry.pack(side='top', anchor="center", pady= 20)

    #== Data View ================================ 

    def configure_frameDataView(self):
        self.frameDataView = Frame(self.frameAppRankEntry, width=500, height=100, bg="white")
        self.frameDataView.pack(side='top', anchor='center', expand=1, fill=BOTH, pady=20)

        self.listboxDataView = Listbox(self.frameDataView, width=300)
        self.scrollbarDataView = Scrollbar(self.frameDataView, command=self.listboxDataView.yview)
        
        self.scrollbarDataView.pack(side=RIGHT, fill='y')
        self.listboxDataView.pack(side=LEFT,  expand=1)
        
        self.listboxDataView.config(yscrollcommand = self.scrollbarDataView.set)

    #=============================================
    #       Timer Tab
    #=============================================

    def configure_frameTabTimer(self):
        self.frameAppTimer = Frame(self.tabControl, bg='#fc8f79')
        self.frameAppTimer.pack(expand=1, fill=BOTH) 
        self.tabControl.add(self.frameAppTimer, text='タイマー')

    #=============================================
    #       Stats Tab
    #=============================================

    def configure_frameTabStats(self):
        self.frameAppStats = Frame(self.tabControl, bg='#073f18')
        self.frameAppStats.pack(expand=1, fill=BOTH)
        self.tabControl.add(self.frameAppStats, text='合計')
    
   
    #=============================================
    #       Commands
    #=============================================

    def cmd_buttonSaveChange(self):
        self.buttonSaveChange.config(state=DISABLED)

    def cmd_buttonEnterData(self):
        studentClass    = self.var_studentClass.get()
        studentNumber   = self.var_studentNumber.get()
        studentRank     = self.var_studentRank.get()

        self.var_studentClass.set('')
        self.var_studentNumber.set('')
        self.var_studentRank.set('')

        #self.listboxDataView.insert(END,f'Class: {studentClass}\t\tNumber: {studentNumber}\t\tRank: {studentRank}')
        print(f'Class: {studentClass}\t\tNumber: {studentNumber}\t\tRank: {studentRank}')

    def cmd_listboxDataView_itemClicked(self):
        pass

    #== File Menu ================================

    def cmd_menuFile_new(self):
        pass

    def cmd_menuFile_open(self):
        pass

    def cmd_menuFile_export(self):
        pass

    def cmd_menuFile_save(self):
        pass

    def cmd_menuFile_saveAs(self):
        pass

    def cmd_menuFile_close(self):
        pass

    #== Settings Menu ============================

    def cmd_menuSettings_language(self):
        pass

    def cmd_menuSettings_keymap(self):
        pass

    #== Help Menu ++++============================

    def cmd_menuHelp_howToUse(self):
        pass

    def cmd_menuHelp_docs(self):
        pass


