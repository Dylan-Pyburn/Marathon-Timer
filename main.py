from tkinter import *

WINDOW_TITLE    = 'マラソン タイマー'
WINDOW_WIDTH    = 1200
WINDOW_HEIGHT   = 700


if __name__ == '__main__':

    root = Tk()
    root.title(WINDOW_TITLE)
    root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
    
    labelHello = Label(root, text='Hello Tkinter World!')

    labelHello.pack()

    root.mainloop()


