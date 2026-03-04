import tkinter as tk
import customtkinter as ctk

from src.view.view_frame import ViewFrame

class AppView(ViewFrame):
    '''
    Main frame of the application. Has the menubar and tabview.
    All other frames should be packed into this frame.

    Accessible attributes:
        tabMeibo
        tabEntry
        tabStats
    '''

    def __init__(self, parent):
        super().__init__(parent)
    
        self.configure_menubar()
        self.configure_tabview()
    
    #=============================================
    #       Tabview
    #=============================================

    def configure_tabview(self):
        self.tabview = ctk.CTkTabview(self)
        
        self.tabMeibo = self.tabview.add('名簿')
        self.tabEntry = self.tabview.add('入力')
        self.tabStats = self.tabview.add('合計')
        
        self.tabview.pack(fill='both', expand=True)

    #=============================================
    #       MenuBar
    #=============================================

    def configure_menubar(self):
        self.menubar = tk.Menu(self)
        self.parent.config(menu=self.menubar)

        self.configure_menubar_file()
        self.configure_menubar_settings()
        self.configure_menubar_help()
                
    def configure_menubar_file(self):
        self.menuFile = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='ファイル', menu=self.menuFile)
        
        self.menuFile.add_command(label='新規',            command=None)
        self.menuFile.add_command(label='開く',            command=None)
        self.menuFile.add_separator()
        self.menuFile.add_command(label='名前を付けて保存', command=None) 
        self.menuFile.add_command(label='保存',            command=None) 
        self.menuFile.add_separator()
        self.menuFile.add_command(label='閉じる',          command=None)
        
    def configure_menubar_settings(self):
        self.menuSettings = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='設定', menu=self.menuSettings)

        self.menuSettings.add_command(label='テーマ',       command=None)
        self.menuSettings.add_command(label='言語',         command=None)
        self.menuSettings.add_command(label='キーマップ',   command=None)

    def configure_menubar_help(self):
        self.menuHelp = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='ヘルプ', menu=self.menuHelp)

        self.menuHelp.add_command(label='使い方', command=None)
        self.menuHelp.add_command(label='Docs',  command=None)

    