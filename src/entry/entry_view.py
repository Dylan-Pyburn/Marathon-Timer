import  tkinter         as tk
from    tkinter         import ttk
import  customtkinter   as ctk
import src.widgets.scrollable_button_frame as sf

class EntryView(ctk.CTkFrame):


    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None

        self.configure_vars()
        self.configure_frames()

        # uncomment if you want to start in dark mode
        # self.switchAppTheme.toggle()  
    
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
        self.configure_dataView()
    
    #=============================================
    #      UI Elements
    #=============================================

    def configure_frameAppTheme(self):
        self.frameAppTheme          = ctk.CTkFrame(self,)

        self.switchAppTheme         = ctk.CTkSwitch(self.frameAppTheme, text='Light / Dark theme',
                                                        command=self.clicked_switchAppTheme)
        
        #---- Placement --------------------------
        self.switchAppTheme.pack(anchor='w')
        self.frameAppTheme.pack(fill='x', padx=20, pady=10)


    def configure_frameFileSelection(self):
        self.frameFileSelection         = ctk.CTkFrame(self,)

        frameMeiboSelection             = ctk.CTkFrame(self.frameFileSelection, )
        self.labelMeiboPath             = ctk.CTkLabel(frameMeiboSelection, text='ファイルを選択してください')
        self.buttonChooseMeiboFile      = ctk.CTkButton(frameMeiboSelection, text='名簿の読み込み',
                                                    command=self.clicked_buttonChooseMeiboFile)
        
        frameEntrySelection             = ctk.CTkFrame(self.frameFileSelection,)
        self.labelEntryPath             = ctk.CTkLabel(frameEntrySelection, text='順位の結果ファイルを選択してください')
        self.buttonChooseEntryFile      = ctk.CTkButton(frameEntrySelection, text='結果ファイルの選択',
                                                    command=self.clicked_buttonChooseEntryFile)
        
        frameTimeDataSelection          = ctk.CTkFrame(self.frameFileSelection)
        self.labelTimeDataPath          = ctk.CTkLabel(frameTimeDataSelection, text='時間データを選択してください')
        self.buttonChooseTimeDataFile   = ctk.CTkButton(frameTimeDataSelection, text='時間データの選択',
                                                    command=self.clicked_buttonChooseEntryFile)

        frameSaveEntries                = ctk.CTkFrame(self.frameFileSelection,)
        self.buttonSaveEntries          = ctk.CTkButton(frameSaveEntries, text='結果の保存',
                                                    command=self.clicked_buttonSaveEntries)

        #---- Placement --------------------------
        # just didn't want to type the same thing many times
        def place(frame, label, button):
            frame.grid_columnconfigure(0,weight=1)
            frame.grid_columnconfigure(1,weight=1)
            frame.pack(side='top', fill='x', pady=4, ipadx=5, ipady=2)
            if label:
                label.grid( row=0, column=0, sticky='w')
            if button:
                button.grid(row=0, column=1, sticky='e')
            #frame.configure(fg_color='grey90')
        
        place(frameMeiboSelection,    self.labelMeiboPath,    self.buttonChooseMeiboFile)
        place(frameEntrySelection,    self.labelEntryPath,    self.buttonChooseEntryFile)
        place(frameTimeDataSelection, self.labelTimeDataPath, self.buttonChooseTimeDataFile)
        place(frameSaveEntries,       None,                   self.buttonSaveEntries)
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

    def configure_dataView(self):
        #---- Meibo/Entries Radios ---------------
        self.frameDataViewRadios    = ctk.CTkFrame(self)
        self.radioMeibo             = ctk.CTkRadioButton(self.frameDataViewRadios, text='名簿', value='meibo',
                                                        variable=self.var_radioDataView, command=self.clicked_radio_display)
        self.radioEntries           = ctk.CTkRadioButton(self.frameDataViewRadios, text='順位データ', value='entry', 
                                                        variable=self.var_radioDataView, command=self.clicked_radio_display)
        self.radioTimerData         = ctk.CTkRadioButton(self.frameDataViewRadios, text='時間データ', value='time', 
                                                        variable=self.var_radioDataView, command=self.clicked_radio_display)
        self.radioResults           = ctk.CTkRadioButton(self.frameDataViewRadios, text='結果', value='results', 
                                                        variable=self.var_radioDataView, command=self.clicked_radio_display)

        #---- ScrollFrame -----------------------        
        frameDataView               = ctk.CTkFrame(self)
        self.scrollFrameDataView    = sf.ScrollableButtonFrame(
            frameDataView, 
            edit_command   = None,
            delete_command = self.clicked_scrollFrameDelete
        )
        
        #--- Filters -----------------------------
        frameDataFilters        = ctk.CTkFrame(frameDataView)
        self.checkButtonMale    = ctk.CTkCheckBox(frameDataFilters, text='男子', command=self.clicked_checkbox_sort,
                                                        variable=self.var_checkboxMale, onvalue=True, offvalue=False)
        self.checkButtonFemale  = ctk.CTkCheckBox(frameDataFilters, text='女子', command=self.clicked_checkbox_sort,
                                                        variable=self.var_checkboxFemale, onvalue=True, offvalue=False)
        separator               = ttk.Separator(frameDataFilters, orient=tk.HORIZONTAL, )
        self.radioNewest        = ctk.CTkRadioButton(frameDataFilters, text='最新', value='newest',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        self.radioOldest        = ctk.CTkRadioButton(frameDataFilters, text='最古', value='oldest',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        self.radioOrderMale     = ctk.CTkRadioButton(frameDataFilters, text='順位：男性', value='sortedMale',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        self.radioOrderFemale   = ctk.CTkRadioButton(frameDataFilters, text='順位：女性', value='sortedFemale',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)

        #---- Placement --------------------------
        self.frameDataViewRadios.pack(side='top', pady=5) # parent is self
        self.radioMeibo.pack(side='left', padx=5)
        self.radioEntries.pack(side='left', padx=5)

        frameDataView.pack(side='top', fill='both', expand=True, pady=10, padx=150) # parent is self
        self.scrollFrameDataView.pack(side='left', fill='both', expand=True, padx=5, pady=(5,15)) # parent is frameDataView
        
        frameDataFilters.pack(side='right',  anchor='center', padx=5) # parent is frameDataView
        self.checkButtonMale.pack(side='top')           
        self.checkButtonFemale.pack(side='top')
        separator.pack(side='top', fill='x', pady=10)
        self.radioNewest.pack(side='top')
        self.radioOldest.pack(side='top')
        self.radioOrderMale.pack(side='top')
        self.radioOrderFemale.pack(side='top')


    def configure_frameDataViewControls(self):
        self.frameDataViewControls  = ctk.CTkFrame(self.frameDataViewDisplay)

        
        #---- Placement --------------------------

   
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

    def clicked_buttonChooseTimeDataFile(self):
        if self.controller:
            self.controller.choose_time_data_file()

    def clicked_scrollFrameEdit(self):
        pass

    def clicked_scrollFrameDelete(self, buttonNum):
        if self.controller:
            self.controller.remove_entry(buttonNum)

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

    def clicked_checkbox_sort(self):
        if self.controller:
            self.controller.handle_checkbutton_sort()

    #==== Key Presses ============================

    def pressed_enter(self, event):
        if self.controller:
            self.controller.add_entry()
            
