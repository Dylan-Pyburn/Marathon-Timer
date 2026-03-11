import  tkinter         as tk
from    tkinter         import ttk
import  customtkinter   as ctk
import src.widgets.scrollable_button_frame as sf

class StatsView(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None

        self.configure_vars()
        self.configure_frames()
    
    def set_controller(self, controller):
        self.controller = controller

    def configure_vars(self):
        pass
    
    def configure_frames(self):
        pass

    #=============================================
    #       UI Elements
    #=============================================

    def configure_frameFileSelection(self):
        self.frameFileSelection         = ctk.CTkFrame(self,)

        frameMeiboSelection             = ctk.CTkFrame(self.frameFileSelection, )
        self.labelMeiboPath             = ctk.CTkLabel(frameMeiboSelection, text='ファイルを選択してください')
        
        frameEntrySelection             = ctk.CTkFrame(self.frameFileSelection,)
        self.labelEntryPath             = ctk.CTkLabel(frameEntrySelection, text='順位の結果ファイルを選択してください')
        
        frameTimeDataSelection          = ctk.CTkFrame(self.frameFileSelection)
        self.labelTimeDataPath          = ctk.CTkLabel(frameTimeDataSelection, text='時間データを選択してください')
        self.buttonChooseTimeDataFile   = ctk.CTkButton(frameTimeDataSelection, text='時間データの選択',
                                                    command=None)

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
        # place(frameEntrySelection,    self.labelEntryPath,    self.buttonChooseEntryFile)
        # place(frameTimeDataSelection, self.labelTimeDataPath, self.buttonChooseTimeDataFile)
        # place(frameSaveEntries,       None,                   self.buttonSaveEntries)
        self.frameFileSelection.pack(fill='x', padx=200, pady=20)
    

    def configure_frameSummary(self):
        pass
    
    
    def configure_frameDataView(self):
        pass

    #=============================================
    #       Commands
    #=============================================
