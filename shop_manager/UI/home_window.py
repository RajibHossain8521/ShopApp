from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#from login_window import Window_1

def main():
    root = Tk()
    app = Home_window(root)

class Home_window:
    """ HOME WINDOW """
    def __init__(self, master):
        self.master = master
        self.master.title("Shop Info")
        self.width = 1366
        self.height = 768
        self.master.geometry("%dx%d" % (self.width, self.height))

        

        self.master.mainloop()


# if __name__ == "__main__":
#     main()