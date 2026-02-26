from tkinter import *

class EntryView(Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None

        self.config(bg='skyblue')

        self.configure_vars()
        self.configure_frameDataEntry()
        self.configure_frameDataView()

        #parent.bind('<Return>', self.pressed_enter)
        #self.bind('<Return>', self.pressed_enter)

    def configure_vars(self):
        self.var_studentClass   = StringVar(self)
        self.var_studentNumber  = StringVar(self)
        self.var_studentRank    = StringVar(self)
    

    def set_controller(self, controller):
        self.controller = controller
    
    #=============================================
    #      UI Elements
    #=============================================

    #== Data Entry =============================== 

    def configure_frameDataEntry(self):
        self.frameDataEntry = Frame(self, width=500, height=150,bg="white")

        self.labelStudentClass      = Label(self.frameDataEntry, text='組')
        self.entryStudentClass      = Entry(self.frameDataEntry, textvariable=self.var_studentClass)

        self.labelStudentNumber     = Label(self.frameDataEntry, text='出席番号')
        self.entryStudentNumber     = Entry(self.frameDataEntry, textvariable=self.var_studentNumber)
        
        self.labelStudentRank       = Label(self.frameDataEntry, text='順位')
        self.entryStudentRank       = Entry(self.frameDataEntry, textvariable=self.var_studentRank)

        self.buttonSaveEntries      = Button(self.frameDataEntry, text='保存',  command=self.clicked_buttonSaveEntries)
        self.buttonEnterData        = Button(self.frameDataEntry, text='追加',  command=self.clicked_buttonEnterData)

        self.labelMessage           = Label(self.frameDataEntry, fg='red')

        self.arrange_frameDataEntry()

    #== Data View ================================

    def arrange_frameDataEntry(self):
        self.labelStudentClass.grid(    row=0,  column=0,   padx=10,    pady=10)
        self.entryStudentClass.grid(    row=1,  column=0,   padx=10,    pady=10)

        self.labelStudentNumber.grid(   row=0,  column=1,   padx=10,    pady=10)
        self.entryStudentNumber.grid(   row=1,  column=1,   padx=10,    pady=10)

        self.labelStudentRank.grid(     row=0,  column=2,   padx=10,    pady=10)
        self.entryStudentRank.grid(     row=1,  column=2,   padx=10,    pady=10)

        self.buttonSaveEntries.grid(    row=0,  column=3,   padx=20,    pady=10)
        self.buttonEnterData.grid(      row=1,  column=3,   padx=20,    pady=10)

        self.labelMessage.grid(         row=3,  column=0,   padx=10,    pady=10)

        self.frameDataEntry.pack(side='top', anchor="center", pady= 20)

    #== Data View ================================ 

    def configure_frameDataView(self):
        self.frameDataView = Frame(self, width=500, height=100, bg="white")
        self.frameDataView.pack(side='top', anchor='center', pady=20)

        self.listboxDataView = Listbox(self.frameDataView, selectmode=SINGLE)
        self.scrollbarDataView = Scrollbar(self.frameDataView, command=self.listboxDataView.yview)
        
        self.scrollbarDataView.pack(side=RIGHT, fill='y')
        self.listboxDataView.pack(side=LEFT, fill=BOTH)
        
        self.listboxDataView.config(yscrollcommand = self.scrollbarDataView.set)

    #=============================================
    #      Commands
    #=============================================

    def pressed_enter(self, event):
        print("enter pressed")
        if self.controller:
            self.controller.clicked_add_entry()

    def clicked_buttonEnterData(self):
        if self.controller:
            self.controller.clicked_add_entry()

    def clicked_buttonSaveEntries(self):
        if self.controller:
            self.controller.clicked_save_entries()

    def clicked_listBoxData(self):
        pass