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
        # SHOP: CUSTOMER AND ACCOUNT INFO
        #================================================
        serial_num = StringVar()
        phone_num = StringVar()
        customer_name = StringVar()
        customer_address = StringVar()
        total_due = StringVar()
        exist_due = StringVar()
        last_payment = StringVar()
        total_shopping = StringVar()

        days_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
         '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

        month_list = ['January', 
                    'February', 
                    'March', 
                    'April', 
                    'May', 
                    'June', 
                    'July', 
                    'August', 
                    'September', 
                    'October', 
                    'November', 
                    'December']
        year_list = ['2020', '2021', '2022', '2023', '2024', '2025']

        customer_info_frame = Frame(
            self.master, 
            bd=3, 
            padx=50, 
            pady=20, 
            bg='#ffe6e6',
            width=600,
            height=605,
            relief=RIDGE
        ).place(x=30, y=40)

        self.personal_info_level = Label(
            self.master,
            bg='yellow',
            text="ব্যক্তিগত তথ্য",
            font=("Courier", 12, 'bold')
        ).place(x=250, y=60)

        self.serial_no_level = Label(
            self.master,
            text="ক্রমিক নং:",
            font=("Courier", 12, 'bold')
        ).place(x=60, y=107)

        self.serial_no_field = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            textvariable=serial_num,
            bd=2,
        )
        self.serial_no_field.pack()
        self.serial_no_field.place(x=180, y=105, height=30, width=170)

        self.phone_no_level = Label(
            self.master,
            text="ফোন নাম্বার:",
            font=("Courier", 12, 'bold')
        ).place(x=43, y=142)

        self.phone_no_field = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            textvariable=phone_num,
            bd=2,
        )
        self.phone_no_field.pack()
        self.phone_no_field.place(x=180, y=140, height=30, width=170)

        self.name_level = Label(
            self.master,
            text="নাম:",
            font=("Courier", 12, 'bold')
        ).place(x=110, y=177)

        self.name_field = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            textvariable=customer_name,
            bd=2,
        )
        self.name_field.pack()
        self.name_field.place(x=180, y=175, height=30, width=170)

        self.address_level = Label(
            self.master,
            text="অ্যাড্রেস:",
            font=("Courier", 12, 'bold')
        ).place(x=75, y=212)

        self.address_field = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            textvariable=customer_address,
            bd=2,
        )
        self.address_field.pack()
        self.address_field.place(x=180, y=210, height=30, width=170)

        self.account_level = Label(
            self.master,
            bg='yellow',
            text="হিসাব",
            font=("Courier", 12, 'bold')
        ).place(x=280, y=270)

        self.last_payment_level = Label(
            self.master,
            text="সর্বশেষ জমা:",
            font=("Courier", 12, 'bold')
        ).place(x=37, y=312)

        self.last_payment_field = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            textvariable=last_payment,
            bd=2,
        )
        self.last_payment_field.pack()
        self.last_payment_field.place(x=180, y=310, height=30, width=170)

        self.exist_due_level = Label(
            self.master,
            text="অবশিষ্ঠ্য:",
            font=("Courier", 12, 'bold')
        ).place(x=73, y=352)

        self.exist_due_field = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            textvariable=exist_due,
            bd=2,
        )
        self.exist_due_field.pack()
        self.exist_due_field.place(x=180, y=350, height=30, width=170)

        self.total_shopping_level = Label(
            self.master,
            text="মোট বাজার:",
            font=("Courier", 12, 'bold')
        ).place(x=43, y=392)

        self.total_shopping_field = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            textvariable=total_shopping,
            bd=2,
        )
        self.total_shopping_field.pack()
        self.total_shopping_field.place(x=180, y=390, height=30, width=170)

        self.total_due_level = Label(
            self.master,
            text="মোট বাকী:",
            font=("Courier", 12, 'bold')
        ).place(x=57, y=432)

        self.total_due_field = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            textvariable=total_due,
            bd=2,
        )
        self.total_due_field.pack()
        self.total_due_field.place(x=180, y=430, height=30, width=170)

        self.customer_info_button = Button(
            self.master, 
            text="সার্চ",
            font=("Courier", 12, 'bold'),
            #command=
        )
        self.customer_info_button.pack()
        self.customer_info_button.place(x=100, y=550, height=30, width=150)

        self.clear_customer_info_button = Button(
            self.master, 
            text="মুছুন",
            font=("Courier", 12, 'bold'),
            #command=
        )
        self.clear_customer_info_button.pack()
        self.clear_customer_info_button.place(x=300, y=550, height=30, width=150)

        #================================================
        # SHOP: Bill Section
        #================================================
        payment_info_frame = Frame(
            self.master,
            bd=3, 
            padx=50, 
            pady=20, 
            bg='#ffe6e6',
            width=600,
            height=300,
            relief=RIDGE
        ).place(x=650, y=40)

        self.bill_info_level = Label(
            self.master,
            bg='yellow',
            text="বিল পরিশোধ",
            font=("Courier", 12, 'bold')
        ).place(x=885, y=60)

        self.serial_no_payment_level = Label(
            self.master,
            text="ক্রমিক নং:",
            font=("Courier", 12, 'bold')
        ).place(x=695, y=107)

        self.serial_no_payment_field = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            #textvariable=,
            bd=2,
        )
        self.serial_no_payment_field.pack()
        self.serial_no_payment_field.place(x=810, y=105, height=30, width=170)

        self.phone_no_payment_level = Label(
            self.master,
            text="ফোন নাম্বার:",
            font=("Courier", 12, 'bold')
        ).place(x=680, y=145)

        self.phone_no_payment_field = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            #textvariable=,
            bd=2,
        )
        self.phone_no_payment_field.pack()
        self.phone_no_payment_field.place(x=810, y=143, height=30, width=170)

        self.payment_level = Label(
            self.master,
            text="জমা:",
            font=("Courier", 12, 'bold')
        ).place(x=738, y=187)

        self.payment_field = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            #textvariable=,
            bd=2,
        )
        self.payment_field.pack()
        self.payment_field.place(x=810, y=185, height=30, width=170)

        self.payment_save_button = Button(
            self.master, 
            text="সেভ",
            font=("Courier", 12, 'bold'),
            #command=
        )
        self.payment_save_button.pack()
        self.payment_save_button.place(x=750, y=290, height=30, width=150)

        self.payment_update_button = Button(
            self.master, 
            text="আপডেট",
            font=("Courier", 12, 'bold'),
            #command=
        )
        self.payment_update_button.pack()
        self.payment_update_button.place(x=950, y=290, height=30, width=150)

        #==============================================
        # SHOP: Add new shopping
        #==============================================
        add_shopping_frame = Frame(
            self.master,
            bd=3, 
            padx=50, 
            pady=20, 
            bg='#ffe6e6',
            width=600,
            height=300,
            relief=RIDGE
        ).place(x=650, y=345)

        self.new_shopping_info_level = Label(
            self.master,
            bg='yellow',
            text="নতুন কেনাকাটা",
            font=("Courier", 12, 'bold')
        ).place(x=880, y=360)

        self.shopping_level_serial_no = Label(
            self.master,
            text="ক্রমিক নং:",
            font=("Courier", 12, 'bold')
        ).place(x=695, y=400)

        self.shopping_field_serial_no = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            #textvariable=,
            bd=2,
        )
        self.shopping_field_serial_no.pack()
        self.shopping_field_serial_no.place(x=810, y=400, height=30, width=170)

        self.shopping_level_phone_no = Label(
            self.master,
            text="ফোন নাম্বার:",
            font=("Courier", 12, 'bold')
        ).place(x=680, y=440)

        self.shopping_field_phone_no = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            #textvariable=,
            bd=2,
        )
        self.shopping_field_phone_no.pack()
        self.shopping_field_phone_no.place(x=810, y=440, height=30, width=170)

        self.total_shopping_level = Label(
            self.master,
            text="জমা:",
            font=("Courier", 12, 'bold')
        ).place(x=738, y=485)

        self.total_shopping_field = Entry(
            self.master,
            font = ('Courier', 14, 'bold'),
            #textvariable=,
            bd=2,
        )
        self.total_shopping_field.pack()
        self.total_shopping_field.place(x=810, y=485, height=30, width=170)

        shopping_day = StringVar()
        shopping_day.set(days_list[0])

        self.shopping_days_menu = OptionMenu(self.master, shopping_day, *days_list)
        self.shopping_days_menu.pack()
        self.shopping_days_menu.config(font=('Courier', '12', 'bold'))
        self.shopping_days_menu.place(x=760, y=530)

        shopping_month = StringVar()
        shopping_month.set(month_list[0])

        self.shopping_month_menu = OptionMenu(self.master, shopping_month, *month_list)
        self.shopping_month_menu.pack()
        self.shopping_month_menu.config(width=8, font=('Courier', '12', 'bold'))
        self.shopping_month_menu.place(x=830, y=530)

        shopping_year = StringVar()
        shopping_year.set(year_list[0])

        self.shopping_year_menu = OptionMenu(self.master, shopping_year, *year_list)
        self.shopping_year_menu.pack()
        self.shopping_year_menu.config(font=('Courier', '12', 'bold'))
        self.shopping_year_menu.place(x=960, y=530)

        self.shopping_save_button = Button(
            self.master, 
            text="সেভ",
            font=("Courier", 12, 'bold'),
            #command=
        )
        self.shopping_save_button.pack()
        self.shopping_save_button.place(x=750, y=590, height=30, width=150)

        self.shopping_update_button = Button(
            self.master, 
            text="আপডেট",
            font=("Courier", 12, 'bold'),
            #command=
        )
        self.shopping_update_button.pack()
        self.shopping_update_button.place(x=950, y=590, height=30, width=150)

        #==============================================
        # SHOP: Shopping list
        #==============================================
        add_shopping_frame = Frame(
            self.master,
            bd=3,
            padx=50, 
            pady=20, 
            bg='#ffe6e6',
            width=600,
            height=605,
            relief=RIDGE
        ).place(x=1270, y=40)

        self.new_shopping_info_level = Label(
            self.master,
            bg='yellow',
            text="বাজার তথ্য",
            font=("Courier", 12, 'bold')
        ).place(x=1530, y=60)

        selected_month = StringVar()
        selected_month.set(month_list[0])

        self.month_menu = OptionMenu(self.master, selected_month, *month_list)
        self.month_menu.pack()
        self.month_menu.config(width=8, font=('Courier', '12', 'bold'))
        self.month_menu.place(x=1375, y=590)

        selected_year = StringVar()
        selected_year.set(year_list[0])

        self.year_menu = OptionMenu(self.master, selected_year, *year_list)
        self.year_menu.pack()
        self.year_menu.config(font=('Courier', '12', 'bold'))
        self.year_menu.place(x=1510, y=590)

        self.shopping_update_button = Button(
            self.master, 
            text="সার্চ",
            font=("Courier", 12, 'bold'),
            #command=
        )
        self.shopping_update_button.pack()
        self.shopping_update_button.place(x=1605, y=590, height=32, width=100)


if __name__ == "__main__":
    main()