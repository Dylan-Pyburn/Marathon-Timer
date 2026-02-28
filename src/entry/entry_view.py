import tkinter      as tk

from tkinter import ttk

class EntryView(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None

        self.configure_vars()
        self.configure_frames()

    def set_controller(self, controller):
        self.controller = controller

    def configure_vars(self):
        self.var_labelMeiboPath = tk.StringVar(self)
        self.var_studentClass   = tk.StringVar(self)
        self.var_studentNumber  = tk.StringVar(self)
        self.var_studentRank    = tk.StringVar(self)
        self.var_radioDataView  = tk.StringVar(self, 'meibo')
        self.var_radioDataSort  = tk.StringVar(self, 'newest')
        self.var_checkboxMale   = tk.BooleanVar(self, value=True)
        self.var_checkboxFemale = tk.BooleanVar(self, value=True)
    
    def configure_frames(self):
        self.configure_frameFileSelection()
        self.configure_frameDataEntry()
        self.configure_frameMessage()
        self.configure_frameDataView()
        self.configure_frameDataViewControls()
    
    #=============================================
    #      UI Elements
    #=============================================

    def configure_frameFileSelection(self):
        self.frameFileSelection     = ttk.Frame(self)

        frameMeiboSelection         = ttk.Frame(self.frameFileSelection)
        self.labelMeiboPath         = ttk.Label(frameMeiboSelection, text='ファイルを選択してください')
        self.buttonChooseMeiboFile  = ttk.Button(frameMeiboSelection, text='名簿の読み込み',
                                                    command=self.clicked_buttonChooseMeiboFile)
        
        frameEntrySelection         = ttk.Frame(self.frameFileSelection)
        self.labelEntryPath         = ttk.Label(frameEntrySelection, text='順位の結果ファイルを選択してください')
        self.buttonChooseEntryFile  = ttk.Button(frameEntrySelection, text='結果ファイルの選択',
                                                    command=self.clicked_buttonChooseEntryFile)

        frameSaveEntries            = ttk.Frame(self.frameFileSelection)
        self.buttonSaveEntries      = ttk.Button(frameSaveEntries, text='結果の保存',
                                                    command=self.clicked_buttonSaveEntries)

        #---- Placement --------------------------
        # just didn't want to type the same thing many times
        def place(frame, label, button):
            frame.grid_columnconfigure(0,weight=1)
            frame.grid_columnconfigure(1,weight=1)
            frame.pack(side='top', fill='x', pady=4)
            if label:
                label.grid( row=0, column=0, sticky='w')
            if button:
                button.configure(width=18)
                button.grid(row=0, column=1, sticky='e')
        
        place(frameMeiboSelection,  self.labelMeiboPath,    self.buttonChooseMeiboFile)
        place(frameEntrySelection,  self.labelEntryPath,    self.buttonChooseEntryFile)
        place(frameSaveEntries,     None,                   self.buttonSaveEntries)
        self.frameFileSelection.pack(fill='x', padx=200, pady=20)


    def configure_frameDataEntry(self):
        self.frameDataEntry = ttk.Frame(self, width=500, height=150)

        self.labelStudentClass      = ttk.Label(self.frameDataEntry, text='組')
        self.labelStudentNumber     = ttk.Label(self.frameDataEntry, text='出席番号')
        self.labelStudentRank       = ttk.Label(self.frameDataEntry, text='順位')

        self.entryStudentClass      = ttk.Entry(self.frameDataEntry, textvariable=self.var_studentClass)
        self.entryStudentNumber     = ttk.Entry(self.frameDataEntry, textvariable=self.var_studentNumber)
        self.entryStudentRank       = ttk.Entry(self.frameDataEntry, textvariable=self.var_studentRank)

        self.buttonEnterData        = ttk.Button(self.frameDataEntry, text='追加', command=self.clicked_buttonEnterData)
        
        #---- Placement --------------------------
        self.frameDataEntry.pack(side='top', anchor="center", pady=10)

        self.labelStudentClass.grid(        row=0,  column=0,   padx=10,    pady=10)
        self.labelStudentNumber.grid(       row=0,  column=1,   padx=10,    pady=10)
        self.labelStudentRank.grid(         row=0,  column=2,   padx=10,    pady=10)
        
        self.entryStudentClass.grid(        row=1,  column=0,   padx=10,    pady=10)
        self.entryStudentNumber.grid(       row=1,  column=1,   padx=10,    pady=10)
        self.entryStudentRank.grid(         row=1,  column=2,   padx=10,    pady=10)
        self.buttonEnterData.grid(          row=1,  column=3,   padx=20,    pady=10)
    
    def configure_frameMessage(self):
        self.frameMessage   = ttk.Frame(self)
        self.labelMessage   = ttk.Label(self.frameMessage)

        #---- Placement --------------------------
        self.labelMessage.pack()
        self.frameMessage.pack(side='top', padx=200, pady=10)

    def configure_frameDataView(self):
        self.frameDataView          = ttk.Frame(self)

        self.frameDataViewRadios    = ttk.Frame(self.frameDataView)
        self.radioMeibo             = ttk.Radiobutton(self.frameDataViewRadios, text='名簿', value='meibo', 
                                                        variable=self.var_radioDataView, command=self.clicked_radio_display)
        self.radioEntries           = ttk.Radiobutton(self.frameDataViewRadios, text='結果', value='entry', 
                                                        variable=self.var_radioDataView, command=self.clicked_radio_display)

        self.frameDataViewDisplay   = ttk.Frame(self.frameDataView)
        self.listboxDataView        = tk.Listbox(self.frameDataViewDisplay, width=70, height=10, selectmode=tk.SINGLE)
        self.scrollbarDataView      = ttk.Scrollbar(self.frameDataViewDisplay, command=self.listboxDataView.yview)
        
        self.listboxDataView.config(yscrollcommand = self.scrollbarDataView.set)

        #---- Placement --------------------------
        self.frameDataView.pack(side=tk.TOP, pady=10)
        self.frameDataViewRadios.pack(side=tk.TOP)
        self.frameDataViewDisplay.pack(side=tk.LEFT)
        
        self.radioMeibo.pack(side=tk.LEFT, padx=10, pady=10)
        self.radioEntries.pack(side=tk.RIGHT, padx=10, pady=10)

        self.scrollbarDataView.pack(side=tk.RIGHT, fill='y')
        self.listboxDataView.pack(side=tk.LEFT, fill=tk.BOTH)

    def configure_frameDataViewControls(self):
        self.frameDataViewControls  = ttk.Frame(self.frameDataView)

        self.checkButtonMale        = ttk.Checkbutton(self.frameDataViewControls, text='男子', command=self.clicked_checkbutton_sort,
                                                        variable=self.var_checkboxMale, onvalue=True, offvalue=False)
        self.checkButtonFemale      = ttk.Checkbutton(self.frameDataViewControls, text='女子', command=self.clicked_checkbutton_sort,
                                                        variable=self.var_checkboxFemale, onvalue=True, offvalue=False)
        separator                   = ttk.Separator(self.frameDataViewControls, orient=tk.HORIZONTAL)
        self.radioNewest            = ttk.Radiobutton(self.frameDataViewControls, text='最新', value='newest',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        self.radioOldest            = ttk.Radiobutton(self.frameDataViewControls, text='最古', value='oldest',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        self.radioOrderMale         = ttk.Radiobutton(self.frameDataViewControls, text='順位：男性', value='sortedMale',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        self.radioOrderFemale       = ttk.Radiobutton(self.frameDataViewControls, text='順位：女性', value='sortedFemale',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        
        #---- Placement --------------------------
        self.frameDataViewControls.pack(side=tk.RIGHT)

        self.checkButtonMale.pack(side=tk.TOP)
        self.checkButtonFemale.pack(side=tk.TOP)
        separator.pack(side=tk.TOP, pady=5)
        self.radioNewest.pack(side=tk.TOP)
        self.radioOldest.pack(side=tk.TOP)
        self.radioOrderMale.pack(side=tk.TOP)
        self.radioOrderFemale.pack(side=tk.TOP)
   
    #=============================================
    #      Commands
    #=============================================

    def clicked_buttonChooseMeiboFile(self):
        if self.controller:
            self.controller.choose_meibo_file()

    def clicked_buttonChooseEntryFile(self):
        if self.controller:
            self.controller.choose_entry_file()

    def clicked_buttonEnterData(self):
        if self.controller:
            self.controller.add_entry()

    def clicked_buttonSaveEntries(self):
        if self.controller:
            self.controller.save_entries()

    def clicked_radio_display(self):
        if self.controller:
            self.controller.handle_radio_display()

    def clicked_radio_sort(self):
        if self.controller:
            self.controller.handle_radio_sort()

    def clicked_checkbutton_sort(self):
        if self.controller:
            self.controller.handle_checkbutton_sort()

    def clicked_listBoxData(self):
        pass

    #==== Key Presses ============================

    def pressed_enter(self, event):
        if self.controller:
            self.controller.add_entry()
            
