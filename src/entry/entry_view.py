import tkinter      as tk

from tkinter import ttk

import customtkinter    as ctk

class EntryView(ctk.CTkFrame):

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
        self.var_radioAppTheme  = tk.StringVar(self, 'light')
        self.var_radioDataView  = tk.StringVar(self, 'meibo')
        self.var_radioDataSort  = tk.StringVar(self, 'newest')
        self.var_checkboxMale   = tk.BooleanVar(self, value=True)
        self.var_checkboxFemale = tk.BooleanVar(self, value=True)
    
    def configure_frames(self):
        self.configure_frameAppTheme()
        self.configure_frameFileSelection()
        self.configure_frameDataEntry()
        self.configure_frameMessage()
        self.configure_frameDataView()
        self.configure_frameDataViewControls()
    
    #=============================================
    #      UI Elements
    #=============================================

    def configure_frameAppTheme(self):
        self.frameAppTheme          = ctk.CTkFrame(self)

        self.switchAppTheme         = ctk.CTkSwitch(self.frameAppTheme, text='Light / Dark theme',
                                                        command=self.clicked_switchAppTheme)
        
        # uncomment if you want to start in dark mode
        #self.switchAppTheme.toggle()
        
        #---- Placement --------------------------
        self.switchAppTheme.pack(anchor='w')
        self.frameAppTheme.pack(fill='x', padx=20, pady=10)


    def configure_frameFileSelection(self):
        self.frameFileSelection     = ctk.CTkFrame(self)

        frameMeiboSelection         = ctk.CTkFrame(self.frameFileSelection)
        self.labelMeiboPath         = ctk.CTkLabel(frameMeiboSelection, text='ファイルを選択してください')
        self.buttonChooseMeiboFile  = ctk.CTkButton(frameMeiboSelection, text='名簿の読み込み',
                                                    command=self.clicked_buttonChooseMeiboFile)
        
        frameEntrySelection         = ctk.CTkFrame(self.frameFileSelection)
        self.labelEntryPath         = ctk.CTkLabel(frameEntrySelection, text='順位の結果ファイルを選択してください')
        self.buttonChooseEntryFile  = ctk.CTkButton(frameEntrySelection, text='結果ファイルの選択',
                                                    command=self.clicked_buttonChooseEntryFile)

        frameSaveEntries            = ctk.CTkFrame(self.frameFileSelection)
        self.buttonSaveEntries      = ctk.CTkButton(frameSaveEntries, text='結果の保存',
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
                button.grid(row=0, column=1, sticky='e')
        
        place(frameMeiboSelection,  self.labelMeiboPath,    self.buttonChooseMeiboFile)
        place(frameEntrySelection,  self.labelEntryPath,    self.buttonChooseEntryFile)
        place(frameSaveEntries,     None,                   self.buttonSaveEntries)
        self.frameFileSelection.pack(fill='x', padx=200, pady=20)


    def configure_frameDataEntry(self):
        self.frameDataEntry = ctk.CTkFrame(self, width=500, height=150)

        self.labelStudentClass      = ctk.CTkLabel(self.frameDataEntry, text='組')
        self.labelStudentNumber     = ctk.CTkLabel(self.frameDataEntry, text='出席番号')
        self.labelStudentRank       = ctk.CTkLabel(self.frameDataEntry, text='順位')

        self.entryStudentClass      = ctk.CTkEntry(self.frameDataEntry, textvariable=self.var_studentClass)
        self.entryStudentNumber     = ctk.CTkEntry(self.frameDataEntry, textvariable=self.var_studentNumber)
        self.entryStudentRank       = ctk.CTkEntry(self.frameDataEntry, textvariable=self.var_studentRank)

        self.buttonEnterData        = ctk.CTkButton(self.frameDataEntry, text='追加', command=self.clicked_buttonEnterData)
        
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
        self.frameMessage   = ctk.CTkFrame(self)
        self.labelMessage   = ctk.CTkLabel(self.frameMessage)

        #---- Placement --------------------------
        self.labelMessage.pack()
        self.frameMessage.pack(side='top', padx=200, pady=10)

    def configure_frameDataView(self):
        self.frameDataView          = ctk.CTkFrame(self)

        self.frameDataViewRadios    = ctk.CTkFrame(self.frameDataView)
        self.radioMeibo             = ctk.CTkRadioButton(self.frameDataViewRadios, text='名簿', value='meibo', 
                                                        variable=self.var_radioDataView, command=self.clicked_radio_display)
        self.radioEntries           = ctk.CTkRadioButton(self.frameDataViewRadios, text='結果', value='entry', 
                                                        variable=self.var_radioDataView, command=self.clicked_radio_display)

        self.frameDataViewDisplay   = ctk.CTkFrame(self.frameDataView)
        self.listboxDataView        = tk.Listbox(self.frameDataViewDisplay, width=70, height=10, selectmode=tk.SINGLE)
        self.scrollbarDataView      = ctk.CTkScrollbar(self.frameDataViewDisplay, command=self.listboxDataView.yview)
        
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
        self.frameDataViewControls  = ctk.CTkFrame(self.frameDataView)

        self.checkButtonMale        = ctk.CTkCheckBox(self.frameDataViewControls, text='男子', command=self.clicked_checkbutton_sort,
                                                        variable=self.var_checkboxMale, onvalue=True, offvalue=False)
        self.checkButtonFemale      = ctk.CTkCheckBox(self.frameDataViewControls, text='女子', command=self.clicked_checkbutton_sort,
                                                        variable=self.var_checkboxFemale, onvalue=True, offvalue=False)
        separator                   = ttk.Separator(self.frameDataViewControls, orient=tk.HORIZONTAL)
        self.radioNewest            = ctk.CTkRadioButton(self.frameDataViewControls, text='最新', value='newest',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        self.radioOldest            = ctk.CTkRadioButton(self.frameDataViewControls, text='最古', value='oldest',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        self.radioOrderMale         = ctk.CTkRadioButton(self.frameDataViewControls, text='順位：男性', value='sortedMale',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        self.radioOrderFemale       = ctk.CTkRadioButton(self.frameDataViewControls, text='順位：女性', value='sortedFemale',
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

    def clicked_switchAppTheme(self):
        if self.controller:
            self.controller.switch_app_theme()

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
            
