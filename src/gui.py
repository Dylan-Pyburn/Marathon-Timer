from tkinter import *

WINDOW_TITLE    = 'マラソン タイマー'
WINDOW_WIDTH    = 1200
WINDOW_HEIGHT   = 700


class GUI:

    def __init__(self):
        self.configure_gui()

    #== Widgets ================================== 

    def configure_gui(self):
        self.configure_root()
        self.configure_frameDataEntry()
        self.configure_frameDataView()
        
    def configure_root(self):
        self.root = Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.root.config(bg='skyblue')

    def configure_frameDataEntry(self):
        self.frameDataEntry = Frame(self.root, width=700, height=150,bg="white")
        self.frameDataEntry.pack(side='top', anchor="center", pady= 20)

    def configure_frameDataView(self):
        self.frameDataView = Frame(self.root, width=700, height=300, bg="white")
        self.frameDataView.pack(side='top', anchor='center', pady=20)


    #== Commands ================================= 


