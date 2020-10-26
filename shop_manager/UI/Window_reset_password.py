from tkinter import *

# Append lib path to system path
sys.path.append('C:/Users/HP/Desktop/ShopApp/shop_manager/lib')
# Local Packages
from password_reset_mail import *


def password_reset_window():
    """ Design Code : New password window"""

    reset_window = Tk()
    reset_window.title("Reset Password")

    # getting screen's height & width in pixels
    sc_h = reset_window.winfo_screenheight()
    sc_w = reset_window.winfo_screenwidth()
    # Set app window size dynamically
    reset_window.geometry("%dx%d" % (sc_w//2, sc_h))

    greetings = Label(reset_window, text="Set New Password!")
    greetings.config(font=("Courier", 30))
    greetings.place(x=100, y=30)

    # Run : Reset Window
    reset_window.mainloop()


if __name__ == "__main__":
    password_reset_window()
