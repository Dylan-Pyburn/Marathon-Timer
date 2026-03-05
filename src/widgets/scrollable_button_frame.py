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

    def __init__(self, parent, edit_command=None, delete_command=None, **kwargs) ->None:
        ''' 
        Constructor
        params:
            parent:     the parent wdiget
            command:    a command that will take the pressed button number as an argument
                            ex: command = handle_button(buttonNum)
        '''
        super().__init__(parent, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(1, weight=1)
        self.configure(border_width=1)
        
        self.edit_command   = edit_command
        self.delete_command = delete_command
        self.rows           = []

    def set_edit_command(self, newCommand:function):
        '''
        Command must be a function that takes one argument (the row number).
        '''
        if not isinstance(newCommand, function):
            raise TypeError(f'ScrollFrame: command must be a function, was {type(newCommand)}')
        self.edit_command = newCommand

    def set_delete_command(self, newCommand:function):
        '''
        Command must be a function that takes one argument (the row number).
        '''
        if not isinstance(newCommand, function):
            raise TypeError(f'ScrollFrame: command must be a function, was {type(newCommand)}')
        self.delete_command = newCommand

    def add_item(self, item:str, showDelBtn:bool=True):
        '''
        Add an item to the bottom of the list.
        params:
            item    : the item to be added in string form
        '''
        label  = self._make_item_button(self, item)
        button = self._make_delete_button(self)

        label.grid(row=len(self.rows), column=0, sticky='w')
        if showDelBtn:
            button.grid(row=len(self.rows), column=1, sticky='e')

        self.rows.append((label, button))
    

    def get_item(self, rowNum:int):
        '''
        Return the name of the text of the given itemNum
        '''
        if rowNum < 0 or rowNum >= len(self.rows):
            return
        
        label, _ = self.rows[rowNum]
        return label

    
    def get_item_str(self, rowNum:int):
        label = self.get_item(rowNum)

        if not label:
            return ''
        
        return label.cget('text')
    
    
    def edit_item(self, itemNum:int, newItem:str):
        '''
        Change the text of a given row.
        '''
        label, _ = self.rows[itemNum]
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
        for i, row in enumerate(self.rows):
            label, button = row
            if self.edit_command:
                label.configure(command=lambda: self.edit_command(i))
            if self.delete_command:
                button.configure(command=lambda: self.delete_command(i))

    def _make_label(self, text):
        return ctk.CTkLabel(self, 
            text=text, 
            compound="left", 
            padx=5, 
            anchor="w",
            font=ctk.CTkFont(size=20)
        )

    def _make_item_button(self, parent, item) -> ctk.CTkButton:
        button = ctk.CTkButton(
            parent, 
            text            = item,
            corner_radius   = 0, 
            hover_color     = '#bab7b6',
            fg_color        = 'transparent',     
            text_color      = 'black',
            font            = ctk.CTkFont(size=14,)
        )
        if self.edit_command:
            x = len(self.rows)
            button.configure(command=lambda: self.edit_command(x))
        return button

    def _make_delete_button(self, parent) -> ctk.CTkButton:
        button  = ctk.CTkButton(
            parent,
            text='X',
            anchor          = 'center', 
            width           = 5, 
            corner_radius   = 100, 
            hover_color     = '#fcdad9', 
            fg_color        = 'transparent',     
            text_color      = 'red', 
            font            = ctk.CTkFont(size=20, weight='bold')
        )
        if self.delete_command:
            x = len(self.rows)
            button.configure(command=lambda: self.delete_command(x))
        return button

