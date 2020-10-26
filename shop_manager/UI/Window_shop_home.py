from tkinter import *


def shop_home_window():
    
    home_window = Tk()
    home_window.title("Home Window")

    sc_wigth = home_window.winfo_screenwidth()
    sc_height = home_window.winfo_screenheight()

    home_window.geometry("%dx%d" % (sc_wigth, sc_height))

    # Run shop home window
    home_window.mainloop()