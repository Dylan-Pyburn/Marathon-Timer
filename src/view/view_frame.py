import customtkinter as ctk

class ViewFrame(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.controller = None
        
    def set_controller(self, controller):
        self.controller = controller

    def configure_vars(self):
        raise NotImplementedError
    
    def configure_frames(self):
        raise NotImplementedError