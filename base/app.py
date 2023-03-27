from threading import *
from root import *
from gui import gui
from test import test



def main(args= None):
    
    root = root_()
    app = test(root)
    #app = gui(root)
    #app.daemon = True

    print("gui launched")
    root.mainloop()
    #gui.stop()


if __name__ == '__main__':
    main()
    #print("app closed")