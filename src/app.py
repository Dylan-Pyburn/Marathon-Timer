'''
App Class
    Main starting point for the app
    Controller for the GUI

APPクラス
    GUI のコントローラー
'''

from src.view import View

class App:
    
    def __init__(self):
        self.view = View()


    def start(self):
        self.view.root.mainloop()




