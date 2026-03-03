'''
Adapted from 
    https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/scrollable_frame_example.py
'''

import customtkinter as ctk

class ScrollableButtonFrame(ctk.CTkScrollableFrame):
    '''
    Add editing and deletion to CTkScrollableFrame.
    The best part? You can easily know which button was clicked!

    Currently only supports strings for the label.
    '''

    def __init__(self, parent, command:function=None, **kwargs) ->None:
        ''' 
        Constructor
        params:
            parent:     the parent wdiget
            command:    a command that will take the pressed button number as an argument
                            ex: command = handle_button(buttonNum)
        '''
        super().__init__(parent, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.configure(border_width=1)
        
        self.command = command
        self.rows    = []


    def add_item(self, item:str, showDelBtn:bool=True):
        '''
        Add an item to the bottom of the list.
        params:
            item    : the item to be added in string form
        '''
        label  = self._make_label(item)
        button = self._make_delete_button()

        # add to the end of the list (the bottom)
        label.grid(row=len(self.rows), column=0, pady=(0, 10), sticky="w")
        if showDelBtn:
            button.grid(row=len(self.rows), column=1, pady=(0, 10), padx=5)

        self.rows.append((label, button))
    

    def get_item(self, rowNum:int):
        '''
        Return the name of the text of the given itemNum
        '''
        if rowNum < 0 or rowNum >= len(self.rows):
            return
        
        label, _ = self.rows[rowNum]
        return label
    
    
    def edit_item(self, itemNum:int, newItem:str):
        '''
        TODO
        Update the text of the given itemNum
        '''
        return

        if itemNum < 0 or itemNum >= len(self.items):
            return
        
        label = self.items[itemNum]
        label.configure(text=newItem)


    def remove_item(self, rowNum):
        '''
        Delete itemNum.
        '''
        if rowNum < 0 or rowNum >= len(self.rows):
            return

        item, button = self.rows[rowNum]

        item.destroy()
        button.destroy()
        del self.rows[rowNum]
        
        self._update_button_nums()


    def clear(self):
        '''
        Remove all items
        '''
        if len(self.rows) == 0:
            return

        for item, button in self.rows:
            item.destroy()
            button.destroy()
        self.rows.clear()

    #=============================================
    #       Widgets
    #=============================================

    def _update_button_nums(self):
        if not self.command:
            return
        
        for i, row in enumerate(self.rows):
            _, button = row
            button.configure(command=lambda: self.command(i))

    def _make_label(self, text):
        return ctk.CTkLabel(self, 
            text=text, 
            compound="left", 
            padx=5, 
            anchor="w",
            font=ctk.CTkFont(size=20)
        )

    def _make_delete_button(self) -> ctk.CTkButton:
        button  = ctk.CTkButton(self, 
            text='X',
            anchor          = 'center', 
            width           = 5, 
            corner_radius   = 100, 
            hover_color     = '#fcdad9', 
            fg_color        = 'transparent',     
            text_color      = 'red', 
            font            = ctk.CTkFont(size=20, weight='bold')
        )
        if self.command:
            x = len(self.rows)
            button.configure(command=lambda: self.command(x))
        return button

