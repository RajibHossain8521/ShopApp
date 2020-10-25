from tkinter import *
from PIL import Image, ImageTk

# Local Packages
import Window_reset_password

def login(password):
    """ Function : For verifying user password """
    with open("C:\\Users\\HP\\Desktop\\ShopApp\\shop_manager\\sources\\login.txt", "r+") as log:
        check_password = log.read()
        print(check_password)    


def main_window():
    # main window of shop app project

    main_window = Tk()
    main_window.title("Login")

    # getting screen's height in pixels 
    h = main_window.winfo_screenheight() 
    # getting screen's width in pixels 
    w = main_window.winfo_screenwidth() 
    # Set app window size dynamically
    main_window.geometry("%dx%d" % (w,h))

    # Set background Image
    impage_file_path = 'C:\\Users\\HP\\Desktop\\ShopApp\\shop_manager\\sources\\login_page_photo.jpg'
    main_window_image = Image.open(impage_file_path)
    main_window_image = main_window_image.resize((w//2, h), Image.ANTIALIAS)
    main_window_image = ImageTk.PhotoImage(main_window_image)
    l = Label(image=main_window_image, anchor=W)
    l.pack(fill=BOTH, expand=True)

    # Greetings Text
    greetings = Label(main_window, text = "Welcome to Shop App!") 
    greetings.config(font =("Courier", 30))
    greetings.place(x = w//2+50, y = 80)

    # Developer Info
    developer_name = Label(main_window, text = "Developed By: Mohammad Rajib",)
    developer_name.config(font =("Courier", 15))
    developer_name.place(x = w//2+150, y=h-120)

    # Password field
    pass_name = Label(main_window, text = "Password")
    pass_name.config(font =("Courier", 15))
    pass_name.place(x = w//2+100, y = 210)
    password_field = Entry(main_window, bd = 3, show="*")
    password_field.place(x = w//2+240, y = 210, height=30, width=150)

    # Button : Password Enter
    password_entry = Button(main_window, text = "Enter")
    password_entry.place(x = w//2+240, y = 250, height=30, width=150)

    # Button : Set new password
    new_password_button = Button(main_window,
                                text="Set New Password",
                                command=Window_reset_password.new_password_window
                                )
    new_password_button.place(x = w//2+240, y=300, height=30, width=150)

    # Run tkinter window
    main_window.mainloop()

if __name__ == "__main__":
    main_window()
    login(123)