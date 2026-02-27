from tkinter import *
from tkinter import ttk


class EntryView(Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None

        self.config(bg='skyblue')

        self.configure_vars()
        self.configure_frames()

    def set_controller(self, controller):
        self.controller = controller


    def configure_vars(self):
        self.var_studentClass   = StringVar(self)
        self.var_studentNumber  = StringVar(self)
        self.var_studentRank    = StringVar(self)
        self.var_radioDataView  = StringVar(self, 'meibo')
        self.var_radioDataSort  = StringVar(self, 'newest')
        self.var_checkboxMale   = BooleanVar(self, value=True)
        self.var_checkboxFemale = BooleanVar(self, value=True)
    
    def configure_frames(self):
        self.configure_frameFileSelection()
        self.configure_frameDataEntry()
        self.configure_frameSaveEntries()
        self.configure_frameDataView()
        self.configure_frameDataViewControls()
    
    #=============================================
    #      UI Elements
    #=============================================

    def configure_frameFileSelection(self):
        self.frameFileSelection     = Frame(self, bg="white")

        self.labelMeiboPath         = Label(self.frameFileSelection, text='名簿を選択してください')
        self.labelEntryPath         = Label(self.frameFileSelection, text='順位の結果ファイルを選択してください')

        self.buttonChooseMeiboFile  = Button(self.frameFileSelection, text='名簿の読み込み', command=self.clicked_buttonChooseMeiboFile)
        self.buttonChooseEntryFile  = Button(self.frameFileSelection, text='結果ファイルの選択', command=self.clicked_buttonChooseEntryFile)

        #---- Placement --------------------------
        self.frameFileSelection.pack(side=TOP, pady=10)

        self.labelMeiboPath.grid(           row=0, column=0, padx=10, pady=10)
        self.labelEntryPath.grid(           row=1, column=0, padx=10, pady=10)
        self.buttonChooseMeiboFile.grid(    row=0, column=1, padx=10, pady=10)
        self.buttonChooseEntryFile.grid(    row=1, column=1, padx=10, pady=10)


    def configure_frameDataEntry(self):
        self.frameDataEntry = Frame(self, width=500, height=150, bg="white")

        self.labelStudentClass      = Label(self.frameDataEntry, text='組')
        self.labelStudentNumber     = Label(self.frameDataEntry, text='出席番号')
        self.labelStudentRank       = Label(self.frameDataEntry, text='順位')

        self.entryStudentClass      = Entry(self.frameDataEntry, textvariable=self.var_studentClass)
        self.entryStudentNumber     = Entry(self.frameDataEntry, textvariable=self.var_studentNumber)
        self.entryStudentRank       = Entry(self.frameDataEntry, textvariable=self.var_studentRank)

        self.buttonEnterData        = Button(self.frameDataEntry, text='追加', command=self.clicked_buttonEnterData)
        
        #---- Placement --------------------------
        self.frameDataEntry.pack(side='top', anchor="center", pady=10)

        self.labelStudentClass.grid(        row=0,  column=0,   padx=10,    pady=10)
        self.labelStudentNumber.grid(       row=0,  column=1,   padx=10,    pady=10)
        self.labelStudentRank.grid(         row=0,  column=2,   padx=10,    pady=10)
        
        self.entryStudentClass.grid(        row=1,  column=0,   padx=10,    pady=10)
        self.entryStudentNumber.grid(       row=1,  column=1,   padx=10,    pady=10)
        self.entryStudentRank.grid(         row=1,  column=2,   padx=10,    pady=10)
        self.buttonEnterData.grid(          row=1,  column=3,   padx=20,    pady=10)

    
    def configure_frameSaveEntries(self):
        self.frameSaveEntries       = Frame(self, bg='white')
        
        self.labelMessage           = Label(self.frameSaveEntries)
        self.buttonSaveEntries      = Button(self.frameSaveEntries, text='保存', command=self.clicked_buttonSaveEntries)

        #---- Placement --------------------------
        self.frameSaveEntries.pack(side=TOP, padx=10, pady=10)

        self.labelMessage.pack(side=LEFT, padx=10, pady=10)
        self.buttonSaveEntries.pack(side=RIGHT, padx=10, pady=10)


    def configure_frameDataView(self):
        self.frameDataView          = Frame(self, bg='white')

        self.frameDataViewRadios    = Frame(self.frameDataView)
        self.radioMeibo             = Radiobutton(self.frameDataViewRadios, text='名簿', value='meibo', 
                                                        variable=self.var_radioDataView, command=self.clicked_radio_display)
        self.radioEntries           = Radiobutton(self.frameDataViewRadios, text='結果', value='entry', 
                                                        variable=self.var_radioDataView, command=self.clicked_radio_display)

        self.frameDataViewDisplay   = Frame(self.frameDataView)
        self.listboxDataView        = Listbox(self.frameDataViewDisplay, width=70, height=10, selectmode=SINGLE)
        self.scrollbarDataView      = Scrollbar(self.frameDataViewDisplay, command=self.listboxDataView.yview)
        
        self.listboxDataView.config(yscrollcommand = self.scrollbarDataView.set)

        #---- Placement --------------------------
        self.frameDataView.pack(side=TOP, pady=10)
        self.frameDataViewRadios.pack(side=TOP)
        self.frameDataViewDisplay.pack(side=LEFT)
        
        self.radioMeibo.pack(side=LEFT, padx=10, pady=10)
        self.radioEntries.pack(side=RIGHT, padx=10, pady=10)

        self.scrollbarDataView.pack(side=RIGHT, fill='y')
        self.listboxDataView.pack(side=LEFT, fill=BOTH)

    def configure_frameDataViewControls(self):
        self.frameDataViewControls  = Frame(self.frameDataView)

        self.checkButtonMale        = Checkbutton(self.frameDataViewControls, text='男子', command=self.clicked_checkbutton_sort,
                                                        variable=self.var_checkboxMale, onvalue=True, offvalue=False)
        self.checkButtonFemale      = Checkbutton(self.frameDataViewControls, text='女子', command=self.clicked_checkbutton_sort,
                                                        variable=self.var_checkboxFemale, onvalue=True, offvalue=False)
        separator                   = ttk.Separator(self.frameDataViewControls, orient=HORIZONTAL)
        self.radioNewest            = Radiobutton(self.frameDataViewControls, text='最新', value='newest',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        self.radioOldest            = Radiobutton(self.frameDataViewControls, text='最古', value='oldest',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        self.radioOrderMale         = Radiobutton(self.frameDataViewControls, text='順位：男性', value='sortedMale',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        self.radioOrderFemale       = Radiobutton(self.frameDataViewControls, text='順位：女性', value='sortedFemale',
                                                        variable=self.var_radioDataSort, command=self.clicked_radio_sort)
        
        #---- Placement --------------------------
        self.frameDataViewControls.pack(side=RIGHT)

        self.checkButtonMale.pack(side=TOP)
        self.checkButtonFemale.pack(side=TOP)
        separator.pack(side=TOP, pady=5)
        self.radioNewest.pack(side=TOP)
        self.radioOldest.pack(side=TOP)
        self.radioOrderMale.pack(side=TOP)
        self.radioOrderFemale.pack(side=TOP)

   
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
            
