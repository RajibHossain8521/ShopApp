from tkinter import *
from tkinter import messagebox

# Append lib path to system path
sys.path.append('C:/Users/HP/Desktop/ShopApp/shop_manager/lib')
# Local Packages
from password_reset_mail import *


def send_mail():
    global email_address
    global reset_window

    if check_valid_email_address(email_address):
        email = email_address.get()
        generate_reset_code(email)
        email_address.set("")
    else:
        email_address.set("")
        messagebox.showinfo("Email", "Invalid Email Address")
        

def verify_reset_code():
    global reset_code
    global reset_window
    global new_password

    checking = verify_reset_password_code(reset_code, new_password)
    if checking:
        # raise pop up window for successfully set new password
        messagebox.showinfo("Good Day!", "New Password Set Successfully.")
    if checking != True:
        # Invalid Authentication code! You may create new one
        messagebox.showerror("Verification", "Invalid verificatio code! You may create new one")

        
if __name__ == "__main__":
    
    # password_reset_window()
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
    greetings.place(x=150, y=30)

    # Create label
    mail_text = Label(
        reset_window, 
        text = "Your Mail Address",
        font =("Courier", 14),
    )
    mail_text.pack()
    mail_text.place(x=240, y=170)

    email_address = StringVar()
    # Entry field for User Password
    email_field = Entry(
        reset_window,
        textvariable=email_address,
        bd=3,
    )
    email_field.pack()
    email_field.place(x=240, y=210, height=30, width=200)

    # Button : Password Enter
    email_submit_button = Button(
        reset_window, 
        text="Enter",
        command=send_mail
    )
    email_submit_button.pack()
    email_submit_button.place(x=240, y=250, height=30, width=200)

    # Create label
    verify_text = Label(
        reset_window, 
        text = "Your Verification Code",
        font =("Courier", 14),
    )
    verify_text.pack()
    verify_text.place(x=220, y=300)

    # Run : Reset Window
    reset_window.mainloop()

