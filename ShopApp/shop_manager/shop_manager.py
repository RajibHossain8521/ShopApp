from tkinter import *

def login(password):
    pass


def set_new_password_window():
    # password reset window
    password_reset_window = Tk()
    password_reset_window.title("Reset Password")
    password_reset_window.mainloop()

def main_window():
    # main window of shop app project

    main_window = Tk()
    main_window.title("Shop Manager")
    main_window.geometry("900x600")

    # Greetings Text
    greetings = Label(main_window, text = "Welcome to Shop App!") 
    greetings.config(font =("Courier", 30))
    greetings.place(x = 220, y = 80)

    # Password field
    pass_name = Label(main_window, text = "Password")
    pass_name.config(font =("Courier", 15))
    pass_name.place(x = 290,y = 210)
    password_field = Entry(main_window, bd = 3, show="*")
    password_field.place(x = 400,y = 210, height=30, width=150)

    # Entry Button
    password_entry = Button(main_window, text = "Entry")
    password_entry.place(x = 430, y = 250, height=30, width=100)

    # Set new password
    new_password_button = Button(main_window, text="Set New Password", width=15, command=set_new_password_window)
    new_password_button.place(x=422, y=300)

    # Run tkinter window
    main_window.mainloop()

if __name__ == "__main__":
    main_window()