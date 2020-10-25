from tkinter import *


def new_password_window():
    """ Design Code : New password window"""

    reset_window = Tk()
    reset_window.title("Reset Password")

    # set window size
    reset_window.geometry("600x600")

    greetings = Label(reset_window, text = "Set New Password!") 
    greetings.config(font =("Courier", 30))
    greetings.place(x=100, y=30)

    # Run : Reset Window
    reset_window.mainloop()

if __name__ == "__main__":
    new_password_window()