'''
Adapted from 
    https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/scrollable_frame_example.py
'''

import customtkinter as ctk

class ScrollableButtonFrame(ctk.CTkScrollableFrame):
    '''
    Add editing and deletion to CTkScrollableFrame.
    The best part? You can easily know which button was clicked!
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

        self.command = command

        self.items = []
        self.buttons = []


    def add_item(self, item:str):
        '''
        Add an item to the bottom of the list.
        params:
            item    : the item to be added in string form
        '''
        label   = ctk.CTkLabel(self, text=item, compound="left", padx=5, anchor="w")
        button  = ctk.CTkButton(self, text='X')

        if self.command:
            x = len(self.buttons)
            button.configure(command=lambda: self.command(x))

        # add to the end of the list (the bottom)
        label.grid(row=len(self.items), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.buttons), column=1, pady=(0, 10), padx=5)

        self.items.append(label)
        self.buttons.append(button)
    

    def get_item(self, itemNum:int):
        '''
        Return the name of the text of the given itemNum
        '''
        if itemNum < 0 or itemNum >= len(self.items):
            return
        
        return self.items[itemNum]
    
    
    def edit_item(self, itemNum:int, newItem:str):
        '''
        Update the text of the given itemNum
        '''
        if itemNum < 0 or itemNum >= len(self.items):
            return
        
        label = self.items[itemNum]
        label.configure(text=newItem)


    def remove_item(self, itemNum):
        '''
        Delete itemNum.
        '''
        if itemNum < 0 or itemNum >= len(self.items):
            return

        item = self.items[itemNum]
        button = self.buttons[itemNum]

        item.destroy()
        button.destroy()

        self.items.remove(item)
        self.buttons.remove(button)


    def clear(self):
        '''
        Remove all items
        '''
        if len(self.items) == 0:
            return
        
        for item, button in zip(self.items, self.buttons):
            item.destroy()
            button.destroy()

        self.items.clear()
        self.buttons.clear()


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.buttonClear = ctk.CTkButton(self, text='clear', command=self.handle_clear)
        self.buttonClear.pack()

        self.sf = ScrollableButtonFrame(self, command=self.handle_button)

        self.sf.add_item('hello')
        self.sf.add_item('hi')
        self.sf.add_item('whats up')

        self.sf.pack()

    def handle_button(self, buttonNum):
        #self.sf.remove_item(buttonNum)

        self.sf.edit_item(buttonNum, 'test')

        print(buttonNum)

    def handle_clear(self):
        self.sf.clear()


if __name__ == '__main__':
    app = App()
    app.mainloop()

