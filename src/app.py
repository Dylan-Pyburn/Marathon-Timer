import  tkinter         as  tk
import customtkinter    as ctk
import os

#-- Model ---------------------------------------- 
from src.model.meibo            import Meibo
from src.model.entry_manager    import EntryManager

#-- View ----------------------------------------- 
from src.view.app_view          import AppView

'''TODO'''
from src.view.entry_view       import EntryView

#-- Controller ----------------------------------- 
from src.controller.entry_controller import EntryController


WINDOW_TITLE    = 'マラソン タイマー'
WINDOW_WIDTH    = 1300
WINDOW_HEIGHT   = 800



class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title(WINDOW_TITLE)
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.minsize(800, 650)
        ctk.set_default_color_theme('themes/theme.json')
        ctk.set_appearance_mode('light')

        self.init_temp_dir()
        appFrame = AppView(self)
        appFrame.pack(fill='both', expand=True)

        meibo              = Meibo()
        entryView          = EntryView(appFrame.tabEntry)
        entryModel         = EntryManager()
        entryController    = EntryController(
            view  = entryView, 
            model = entryModel,
            meibo = meibo
        )
        
        entryModel.set_meibo(meibo)

        entryView.set_controller(entryController)
        entryView.pack(expand=True, fill=tk.BOTH)

        self.bind('<Return>', entryView.pressed_enter)

    def init_temp_dir(self):
        if not os.path.isdir('./temp'):
            os.makedirs('./temp')

    def start(self):
        self.mainloop()

if __name__ == '__main__':
    
    App().start()
