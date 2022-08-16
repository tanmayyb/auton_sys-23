from threading import *
from root import *
from gui import gui



def main(args= None):
    
    root = root_()
    app = gui(root)
    #app.daemon = True

    print("gui launched")
    root.mainloop()
    #gui.stop()


if __name__ == '__main__':
    main()
    #print("app closed")