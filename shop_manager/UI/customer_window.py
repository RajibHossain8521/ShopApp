from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def main():
    root = Tk()
    app = Customer_Info_Window(root)
    root.mainloop()


class Customer_Info_Window:
    """ CUSTOMER INFO WINDOW """
    def __init__(self, master):
        self.master = master
        self.master.title("কাস্টমার সেবা")
        self.width = 1920
        self.height = 1080
        self.master.geometry("%dx%d" % (self.width, self.height))

        # Developer Info
        self.developer_name = Label(
            self.master,
            text="Developed By: Mohammad Rajib",
            font=("Courier", 15)
        ).place(x=800, y=self.height-100)

        # Heading Frame
        self.heading = Label(
            self.master,
            text="কাস্টমার সেবা",
            font=("Courier", 15, 'bold'),
            bd=10,
        ).place(x=20,)

        #================================================
        # CUSTOMER AND ACCOUNT INFO
        #================================================

        
        
        customer_info_frame = Frame(
            self.master, 
            bd=3, 
            padx=50, 
            pady=20, 
            bg='white',
            width=600,
            height=600,
            relief=RIDGE
        ).place(x=20, y=40)

        self.personal_info_level = Label(
            self.master,
            bg='yellow',
            text="ব্যক্তিগত তথ্য",
            font=("Courier", 12, 'bold')
        ).place(x=250, y=60)

        self.serial_no_level = Label(
            self.master,
            bg='yellow',
            text="ক্রমিক নং:",
            font=("Courier", 12, 'bold')
        ).place(x=55, y=100)

        self.phone_no_level = Label(
            self.master,
            bg='yellow',
            text="ফোন নাম্বার:",
            font=("Courier", 12, 'bold')
        ).place(x=38, y=135)

        self.name_level = Label(
            self.master,
            bg='yellow',
            text="নাম:",
            font=("Courier", 12, 'bold')
        ).place(x=105, y=170)

        self.address_level = Label(
            self.master,
            bg='yellow',
            text="অ্যাড্রেস:",
            font=("Courier", 12, 'bold')
        ).place(x=70, y=205)

        self.personal_info_level = Label(
            self.master,
            bg='yellow',
            text="হিসাব",
            font=("Courier", 12, 'bold')
        ).place(x=280, y=250)

        self.tota_due_level = Label(
            self.master,
            bg='yellow',
            text="মোট বাকী:",
            font=("Courier", 12, 'bold')
        ).place(x=50, y=300)

        self.exist_due_level = Label(
            self.master,
            bg='yellow',
            text="অবশিষ্ঠ্য:",
            font=("Courier", 12, 'bold')
        ).place(x=68, y=335)

        self.last_payment_level = Label(
            self.master,
            bg='yellow',
            text="সর্বশেষ জমা:",
            font=("Courier", 12, 'bold')
        ).place(x=32, y=370)

        self.total_bazar_level = Label(
            self.master,
            bg='yellow',
            text="মোট বাজার:",
            font=("Courier", 12, 'bold')
        ).place(x=38, y=405)

        #================================================

        payment_info_frame = Frame(
            self.master,
            bd=3, 
            padx=50, 
            pady=20, 
            bg='white',
            width=600,
            height=300,
            relief=RIDGE
        ).place(x=640, y=40)

        add_bazar_frame = Frame(
            self.master,
            bd=3, 
            padx=50, 
            pady=20, 
            bg='white',
            width=600,
            height=300,
            relief=RIDGE
        ).place(x=640, y=345)


if __name__ == "__main__":
    main()