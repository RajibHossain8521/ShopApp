import sys
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Append lib path to system path
sys.path.append('C:/Users/HP/Desktop/ShopApp/shop_manager/lib')
# Local Packages
from login import login_validation
from password_reset_mail import *

global impage_file_path
impage_file_path = 'C:\\Users\\HP\\Desktop\\ShopApp\\shop_manager\\sources\\login_page_photo.jpg'


def main():
    root = Tk()
    app = Window_1(root)

 
class Window_1:
    """ LOGIN WINDOW """
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.width = 1366
        self.height = 768
        self.master.geometry("%dx%d" % (self.width, self.height))

        # Set Login window image
        self.login_window_image = Image.open(impage_file_path)
        self.login_window_image = self.login_window_image.resize((self.width//2, self.height), Image.ANTIALIAS)
        self.login_window_image = ImageTk.PhotoImage(self.login_window_image)
        self.l = Label(image=self.login_window_image, anchor=W)
        self.l.pack(fill=BOTH, expand=True)
        
        self.greetings = Label(
            self.master,
            text="Welcome to Shop App!",
            font=("Courier", 30, 'bold'),
            bd=10,
        ).place(x=self.width//2+50, y=50)

        self.password_level = Label(
            self.master,
            text="Password",
            font=("Courier", 15)
        ).place(x=self.width//2+100, y=210)

        # Entry field for User Password
        self.input_password = StringVar()
        self.password_field = Entry(
            self.master,
            textvariable=self.input_password,
            bd=3,
            show="*")
        self.password_field.pack()
        self.password_field.place(x=self.width//2+240, y=210, height=30, width=150)

        # Button : Password Enter
        self.password_submit_button = Button(
            self.master, 
            text="Enter",
            command=self.check_user_password
        )
        self.password_submit_button.pack()
        self.password_submit_button.place(x=self.width//2+240, y=250, height=30, width=150)

        self.reset_password_button = Button(
            self.master, 
            text="Set New Password",
            command=self.reset_window
        ).place(x=self.width//2+240, y=300, height=30, width=150)

        # Developer Info
        self.developer_name = Label(
            self.master,
            text="Developed By: Mohammad Rajib",
            font=("Courier", 15)
        ).place(x=self.width//2+150, y=self.height-120)

        self.master.mainloop()

    def check_user_password(self):
        if login_validation(self.input_password.get()):
            self.input_password.set("")
            self.master.destroy()
        else:
            self.input_password.set("")
            messagebox.showwarning("Login Info", "Incorrect Password")

    def reset_window(self):
        # Create window widget for Window_2 class
        self.window = Toplevel(self.master)
        self.app = Window_2(self.window)


class Window_2:
    """ PASSWORD RESET WINDOW """
    def __init__(self, master):
        self.master = master
        self.master.title("Password Reset Window")
        self.width = 1366
        self.height = 768
        self.master.geometry("%dx%d" % (self.width//2, self.height))
        self.master.resizable(False, False)
        
        self.greetings = Label(
            self.master,
            text="Set New Password!!",
            font=("Courier", 30, 'bold'),
            bd=10,
        ).place(x=120, y=30)

        # STEP 01: SEND MAIL TO YOUR MAIL ADDRESS FOR VERIFICATION CODE
        self.step_one = Label(
        self.master, 
        text = "STEP: 01",
        font =("Courier", 14, 'bold', 'underline')
        )
        self.step_one.pack()
        self.step_one.place(x=290, y=130)

        # Create label
        self.mail_text = Label(
        self.master, 
        text = "Your Mail Address",
        font =("Courier", 14),
        )
        self.mail_text.pack()
        self.mail_text.place(x=240, y=170)

        self.email_address = StringVar()
        # Entry field for User Password
        self.email_field = Entry(
        self.master,
        textvariable=self.email_address,
        bd=3,
        )
        self.email_field.pack()
        self.email_field.place(x=240, y=210, height=30, width=200)

        # Button : Mail Enter
        self.email_submit_button = Button(
        self.master, 
        text="Enter",
        font=("Courier", 14),
        bd = 3,
        command=self.send_mail
        )
        self.email_submit_button.pack()
        self.email_submit_button.place(x=240, y=250, height=30, width=200)
        # END : STEP 01

        # STEP 02 : ENTER YOUR VERIFICATION CODE AND NEW PASSWORD
        self.step_two = Label(
        self.master, 
        text = "STEP: 02",
        font =("Courier", 14, 'bold', 'underline')
        )
        self.step_two.pack()
        self.step_two.place(x=290, y=310)

        self.verify_text = Label(
        self.master, 
        text = "Verification Code",
        font =("Courier", 14),
        )
        self.verify_text.pack()
        self.verify_text.place(x=240, y=350)

        self.verification_code = StringVar()
        # Entry field for User Password
        self.verification_code_field = Entry(
        self.master,
        textvariable=self.verification_code,
        bd=3,
        )
        self.verification_code_field.pack()
        self.verification_code_field.place(x=240, y=380, height=30, width=200)

         # Create label
        self.password_text = Label(
        self.master, 
        text = "Enter New Password",
        font =("Courier", 14),
        )
        self.password_text.pack()
        self.password_text.place(x=235, y=440)

        self.new_password = StringVar()
        # Entry field for User Password
        self.new_password_field = Entry(
        self.master,
        textvariable=self.new_password,
        bd=3,
        show="*",
        )
        self.new_password_field.pack()
        self.new_password_field.place(x=240, y=470, height=30, width=200)

        # Button : Password Enter
        self.new_password_button = Button(
        self.master, 
        text="Enter",
        font=("Courier", 14),
        bd=3,
        command=self.set_new_password
        )
        self.new_password_button.pack()
        self.new_password_button.place(x=240, y=510, height=30, width=200)
        # END STEP 02

    # SEND MAIL WITH RESET CODE
    def send_mail(self):
        if validate_email_address(self.email_address.get()):
            reset_code_mail(self.email_address.get())
            self.email_address.set("")
        else:
            self.email_address.set("")
            messagebox.showwarning("Mail Info", "Invalid email address")

    # SET NEW PASSWORD AFTER VERIFYING VERIFICATION CODE
    def set_new_password(self):
        if verify_reset_password_code(self.verification_code.get(), self.new_password.get()):
            # raise pop up window for successfully set new password
            messagebox.showinfo("Good Day!", "New Password Set Successfully.")
            self.master.destroy()
        else:
            # Invalid Authentication code! You may create new one
            messagebox.showerror("Verification", "Invalid verificatio code! You may create new one")


if __name__ == "__main__":
    main()