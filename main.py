import  tkinter         as  tk
import customtkinter    as ctk

#-- Model ---------------------------------------- 
from src.model.meibo            import Meibo
from src.model.entry_manager    import EntryManager

#-- View ----------------------------------------- 
from src.view.app_view          import AppView

'''TODO'''
from src.entry.entry_view       import EntryView

#-- Controller ----------------------------------- 
from src.controller.entry_controller import EntryController


WINDOW_TITLE    = 'マラソン タイマー'
WINDOW_WIDTH    = 900
WINDOW_HEIGHT   = 650



class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title(WINDOW_TITLE)
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.minsize(800, 650)
        ctk.set_default_color_theme('themes/theme.json')
        ctk.set_appearance_mode('light')

        meibo = Meibo()

        appFrame = AppView(self)
        appFrame.pack(fill='both', expand=True)

    
        self.entryView         = EntryView(appFrame.tabEntry)
        self.entryModel         = EntryManager()
        self.entryController    = EntryController(
            view  = self.entryView, 
            model = self.entryModel,
            meibo = meibo
        )
        
        self.entryModel.set_meibo(meibo)

        self.entryView.set_controller(self.entryController)
        self.entryView.pack(expand=True, fill=tk.BOTH)

        self.bind('<Return>', self.entryView.pressed_enter)

    def start(self):
        self.mainloop()

if __name__ == '__main__':
    
    App().start()
