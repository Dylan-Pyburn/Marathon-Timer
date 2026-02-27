from src.app import App


#=================================================
#       Main
#=================================================

if __name__ == '__main__':

    App().start()

    '''
    l = [{1:'女', 2:2},{1:'男', 2:2}, {1:'女', 2:1},{1:'男',2:1}]

    l.sort(key=lambda x: x[2])
    print(l)

    l.sort(key=lambda x: x[1], reverse=True)
    print(l)
    '''
