
import customtkinter as ctk

from src.view.app_view import AppView

WINDOW_TITLE    = 'マラソン タイマー'
WINDOW_WIDTH    = 900
WINDOW_HEIGHT   = 650

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title(WINDOW_TITLE)
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        ctk.set_appearance_mode("light")
    
        appview = AppView(self)

        appview.pack(expand=True, fill="both") 

    def start(self):
        self.mainloop()

if __name__ == '__main__':
    
    App().start()

