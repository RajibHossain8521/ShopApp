import sys
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Append lib path to system path
sys.path.append('C:/Users/HP/Desktop/ShopApp/shop_manager/lib')
# Local Packages
from login import login_validation
from Window_shop_home import shop_home_window
from Window_reset_password import password_reset_window


def check_user_password():
    global input_password
    global login_window

    if login_validation(input_password.get()):
        input_password.set("")
        login_window.destroy()
        shop_home_window()
    else:
        input_password.set("")
        messagebox.showwarning("Login Info", "Incorrect Password")


# Driver Code
if __name__ == "__main__":
    """
    Login Window: In this Driver code section we designed login window interface.
    And called login function for checking user password for entry into shop home window.
    """

    # Create login window
    login_window = Tk()
    login_window.title("Login")

    input_password = StringVar()

    # getting screen's height & width in pixels
    h = login_window.winfo_screenheight()
    w = login_window.winfo_screenwidth()
    # Set app window size dynamically
    login_window.geometry("%dx%d" % (w, h))

    # Set background Image
    impage_file_path = 'C:\\Users\\HP\\Desktop\\ShopApp\\shop_manager\\sources\\login_page_photo.jpg'
    login_window_image = Image.open(impage_file_path)
    login_window_image = login_window_image.resize((w//2, h), Image.ANTIALIAS)
    login_window_image = ImageTk.PhotoImage(login_window_image)
    l = Label(image=login_window_image, anchor=W)
    l.pack(fill=BOTH, expand=True)

    # Greetings Text
    greetings = Label(
        login_window,
        text="Welcome to Shop App!",
        font=("Courier", 30)
    ).place(x=w//2+50, y=80)

    # Developer Info
    developer_name = Label(
        login_window,
        text="Developed By: Mohammad Rajib",
        font=("Courier", 15)
    ).place(x=w//2+150, y=h-120)

    # Password field
    pass_name = Label(
        login_window,
        text="Password",
        font=("Courier", 15)
    ).place(x=w//2+100, y=210)

    # Entry field for User Password
    password_field = Entry(
        login_window,
        textvariable=input_password,
        bd=3,
        show="*")
    password_field.pack()
    password_field.place(x=w//2+240, y=210, height=30, width=150)
  
    # Button : Password Enter
    submit_button = Button(
        login_window, 
        text="Enter",
        command=check_user_password
    )
    submit_button.pack()
    submit_button.place(x=w//2+240, y=250, height=30, width=150)

    # Button : Set new password
    new_password_button = Button(
        login_window,
        text="Set New Password",
        command=password_reset_window
    ).place(x=w//2+240, y=300, height=30, width=150)

    # Run tkinter window
    login_window.mainloop()
