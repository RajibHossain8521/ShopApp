from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def main():
    root = Tk()
    app = Customer_Info_Window(root)


class Customer_Info_Window:
    """ CUSTOMER INFO WINDOW """
    def __init__(self, master):
        self.master = master
        self.master.title("কাস্টমার তথ্য")
        self.width = 1366//2
        self.height = 768
        self.master.geometry("%dx%d" % (self.width, self.height))
        self.master.resizable(False, False)

        self.greetings = Label(
            self.master,
            text="কাস্টমার তথ্য",
            font=("Courier", 12, 'bold'),
            bd=10,
        ).place(x=250, y=5)

        

        self.master.mainloop()


if __name__ == "__main__":
    main()