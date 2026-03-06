'''
Adapted from 
    https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/scrollable_frame_example.py
'''

import customtkinter as ctk

class ScrollableButtonFrame(ctk.CTkScrollableFrame):
    '''
    Add editing (not fully implemented yet) and deletion to CTkScrollableFrame.
    The best part? You can easily know which button was clicked!
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
        frame = ctk.CTkFrame(self)

        fields: list[str] = item.split()
        labels: list[ctk.CTkLabel] = [self._make_label(frame, field) for field in fields]

        '''TODO do this with grid'''
        for i, label in enumerate(labels):
            # assume the last two items are names, make the last name wider and align right
            if i == len(labels) - 2:
                label.configure(width=100, anchor='e')
            label.pack(side='left')
            
        button = self._make_delete_button(frame)
        if showDelBtn:
            button.pack(side='right', anchor='e')
            
        frame.pack(fill='x', expand=True, anchor='w')
        
        self.rows.append((frame, labels, button))
        self._color_frames()


    def _add_item_(self, item:str, showDelBtn:bool=True):
        '''
        Add an item to the bottom of the list.
        params:
            item    : the item to be added in string form
            

        For the purposes of this program i am assuming the text is a list 
        of values separated by spaces, the last two of which should always 
        be the student last and first name (large to account for katakana names).
        Split the string and make labels for each ones.
        '''
        frame = ctk.CTkFrame(self,)
        if len(self.rows) % 2 == 1:
            frame.configure(fg_color='grey90')

        #label  = self._make_item_button(frame, item)
        label  = self._make_label(frame, item)
        button = self._make_delete_button(frame)

        frame.pack(fill='x', padx=5, pady=2)        
        label.pack(side='left', fill='x', expand=True,anchor='w')
        if showDelBtn:
            button.pack(side='right', anchor='e')

        self.rows.append((frame, label, button))

    
    def get_item(self, rowNum:int) -> list[ctk.CTkLabel] | None:
        '''
        Return the list of labels of the given row.
        None if rowNum is out of range.
        '''
        if rowNum < 0 or rowNum >= len(self.rows):
            return
        
        _, labels, _ = self.rows[rowNum]
        return labels

    def get_item_str(self, rowNum:int) -> str | None:
        '''
        Return the text from the given row num.
        None if rowNum is out of range.
        '''
        labels = self.get_item(rowNum)

        if not labels:
            return ''
        
        return ' '.join([l.cget('text') for l in labels])
    
    def _edit_item(self, itemNum:int, newItem:str):
        '''
        Change the text of a given row.
        '''
        raise NotImplementedError

        _, label, _ = self.rows[itemNum]
        label.configure(text=newItem)

    def remove_item(self, rowNum):
        '''
        Delete rowNum if it's in range.
        '''
        self._destroy_row(rowNum)
        del self.rows[rowNum]
        self._color_frames()
        self._update_button_nums()

    def clear(self):
        '''
        Remove all items
        '''
        for n in range(len(self.rows)):
            self._destroy_row(n)
        self.rows.clear()

    def _destroy_row(self, rowNum):
        if rowNum < 0 or rowNum >= len(self.rows):
            return

        frame, labels, button = self.rows[rowNum]
        frame.destroy()
        button.destroy()
        for label in labels:
            label.destroy()

    #=============================================
    #       Widgets
    #=============================================

    def _color_frames(self):
        '''
        Set a grey background for odd numbered rows.
        '''
        for i, row in enumerate(self.rows):
            frame, _, _ = row
            if i % 2 == 1:
                frame.configure(fg_color='grey90')

    def _update_button_nums(self):
        for i, row in enumerate(self.rows):
            _, labels, button = row
            for label in labels:
                if self.edit_command:
                    label.configure(command=lambda: self.edit_command(i))
                if self.delete_command:
                    button.configure(command=lambda: self.delete_command(i))

    def _make_label(self, parent, item):
        return ctk.CTkLabel(
            parent,
            text            = item, 
            anchor          = 'w',
            width           = 60,
            padx            = 5, 
            fg_color        = 'transparent',     
            text_color      = ["gray10","#DCE4EE"],
            font            = ctk.CTkFont(size=16, )
        )

    def _make_item_button(self, parent, item) -> ctk.CTkButton:
        button = ctk.CTkButton(
            parent, 
            text            = item,
            anchor          = 'w',
            corner_radius   = 0, 
            hover_color     = '#bab7b6',
            fg_color        = 'transparent',     
            text_color      = ["gray10","#DCE4EE"],
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

