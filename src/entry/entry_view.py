from tkinter import *

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
        self.var_dataViewRadio  = StringVar(self, 'meibo')
    
    def configure_frames(self):
        self.configure_frameFileSelection()
        self.configure_frameDataEntry()
        self.configure_frameSaveEntries()
        self.configure_frameDataView()
    
    #=============================================
    #      UI Elements
    #=============================================

    def configure_frameFileSelection(self):
        self.frameFileSelection     = Frame(self, bg="white")

        self.labelMeiboPath         = Label(self.frameFileSelection, text='名簿を選択してください')
        self.labelEntryPath         = Label(self.frameFileSelection, text='順位の結果ファイルを選択してください')

        self.buttonChooseMeiboFile  = Button(self.frameFileSelection, text='名簿ファイル', command=self.clicked_buttonChooseMeiboFile)
        self.buttonChooseEntryFile  = Button(self.frameFileSelection, text='結果ファイル', command=self.clicked_buttonChooseEntryFile)

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
        self.frameDataView           = Frame(self, bg='white')

        self.frameDataViewRadios     = Frame(self.frameDataView)
        self.radiobuttonMeibo        = Radiobutton(self.frameDataViewRadios, text='名簿', value='meibo', 
                                                        variable=self.var_dataViewRadio, command=self.clicked_radiobutton)
        self.radiobuttonEntries      = Radiobutton(self.frameDataViewRadios, text='結果', value='entry', 
                                                        variable=self.var_dataViewRadio, command=self.clicked_radiobutton)

        self.frameDataViewDisplay    =  Frame(self)
        self.listboxDataView         = Listbox(self.frameDataViewDisplay, selectmode=SINGLE)
        self.scrollbarDataView       = Scrollbar(self.frameDataViewDisplay, command=self.listboxDataView.yview)
        
        self.listboxDataView.config(yscrollcommand = self.scrollbarDataView.set)

        #---- Placement --------------------------
        self.frameDataView.pack(side=TOP, pady=10)
        self.frameDataViewRadios.pack(side=TOP)
        self.frameDataViewDisplay.pack(side=TOP)
        
        self.radiobuttonMeibo.pack(side=LEFT, padx=10, pady=10)
        self.radiobuttonEntries.pack(side=RIGHT, padx=10, pady=10)

        self.scrollbarDataView.pack(side=RIGHT, fill='y')
        self.listboxDataView.pack(side=LEFT, fill=BOTH)

   
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

    def clicked_radiobutton(self):
        if self.controller:
            self.controller.handle_display_radio()

    def clicked_listBoxData(self):
        pass

    #==== Key Presses ============================

    def pressed_enter(self, event):
        print("enter pressed")
        if self.controller:
            self.controller.add_entry()
