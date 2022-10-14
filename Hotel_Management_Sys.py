import random
import string
import tkinter
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox as mgs
import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import requests
import re
import xlsxwriter


class Details:
    def insert_data(self):
        mysqldb = mysql.connector.connect(host="localhost", user="root", passwd="", database="hotel")
        mycursor = mysqldb.cursor()

        box = self.data.get()
        box1 = self.data_1.get()
        box2 = self.data_2.get()
        box3 = self.data_3.get()
        box4 = self.data_4.get()
        box5 = self.data_5.get()
        box6 = self.data_6.get()
        box7 = self.data_7.get()
        box8 = self.data_8.get()
        box9 = self.data_9.get()
        box10 = self.data_10.get()
        box11 = self.data_11.get()
        box12 = self.data_12.get()
        box13 = self.data_13.get()
        box14 = self.data_14.get()
        box15 = self.data_15.get()

        if box == "":
            mgs.showinfo("Alert!", "reference no is missing")
        elif box1 == "":
            mgs.showinfo("Alert!", "First Name is missing")
        elif box2 == "":
            mgs.showinfo("Alert!", "Last Name is missing")
        elif box3 == "":
            mgs.showinfo("Alert!", "Gender is missing")
        elif box4 == "":
            mgs.showinfo("Alert!", "Id Proof is missing")
        elif box5 == "":
            mgs.showinfo("Alert!", "Id No. is missing")
        elif box6 == "":
            mgs.showinfo("Alert!", "Mobile No. is missing")
        elif box7 == "":
            mgs.showinfo("Alert!", "Address is missing")
        elif box8 == "":
            mgs.showinfo("Alert!", "CheckIn Date is missing")
        elif box9 == "":
            mgs.showinfo("Alert!", "CheckOut Date is missing")
        elif box10 == "":
            mgs.showinfo("Alert!", "Room Type is missing")
        elif box11 == "":
            mgs.showinfo("Alert!", "Room No. is missing")
        elif box12 == "":
            mgs.showinfo("Alert!", "Payment Method is missing")
        elif box13 == "":
            mgs.showinfo("Alert!", "Amount is missing")
        elif box8 == box9:
            mgs.showinfo("Alert!", "CheckIn and Checkout Cannot Be Same")
        else:
            try:
                int(box)
            except ValueError:
                mgs.showerror("Error", "Only Integer is excepted Reference Num")
            else:
                try:
                    mycursor.execute("select Ref_No from customer_details")
                    record = mycursor.fetchall()
                    print(record)
                    for ro in record:
                        if ro[0] == box:
                            print('founded', ro[0])
                            mgs.showinfo("Alert!", "Reference No. already Exist")
                            return 0
                except Exception as e:
                    print(e)
                else:
                    try:
                        if not re.match("^[A-Z,a-z]*$", box1):
                            mgs.showerror('Error', "Only letters are allowed in First Name")
                            return 0
                    except ValueError:
                        mgs.showerror("Error", "")
                    else:
                        try:
                            if not re.match("^[A-Z,a-z]*$", box2):
                                mgs.showerror('Error', "Only letters are allowed Last Name")
                                return 0
                        except ValueError:
                            mgs.showerror("Error", "")
                        else:
                            try:

                                if box4 == 'Aadhaar':
                                    int(box5)
                                    if len(box5) != 12:
                                        mgs.showinfo("Alert!", "12 digits are only excpected")
                                        return 0
                            except ValueError:
                                mgs.showerror("Error", "Only Integer are excepted in ID No")
                            else:

                                try:
                                    int(box6)
                                    if len(box6) != 10:
                                        mgs.showinfo("Alert!", "10 digits are only excpected")
                                        return 0
                                except ValueError:
                                    mgs.showerror("Error", "Only Integer are excepted in Mobile number")
                                else:

                                    try:
                                        int(box11)
                                    except ValueError:
                                        mgs.showerror("Error", "Only Integer are excepted in Room No.")
                                    else:
                                        try:
                                            int(box13)
                                        except ValueError:
                                            mgs.showerror("Error", "Only Integer are excepted in Amount")
                                        else:
                                            try:
                                                sql = "INSERT INTO customer_details VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                val = (box, box1, box2, box3, box4, box5, box6, box7, box8, box9, box10, box11, box12, box13, box14, box15)
                                                mycursor.execute(sql, val)
                                                mysqldb.commit()
                                                f = open('D:/python_projects/Bills/' + box1 + '.txt', 'w')
                                                f.write('      Welcome to Hotel Database \n'
                                                        '================Receipt=================\n'
                                                        'Customer ID:       '+box+'\n'
                                                        'Name:              ' + box1 + ' ' + box2 + '\n'
                                                        'CheckIn Date:      ' + box8 + '\n'
                                                        'CheckOut Date:     ' + box9 + '\n'
                                                        'Room Type:         ' + box10 + '\n'
                                                        'Room No.:          ' + box11 + '\n'
                                                        'Payment Type:      ' + box12 + '\n'
                                                        'Amount:            ' + box13 + '/- only\n'
                                                        '=========================================')
                                                f.close()
                                                mgs.showinfo("information", "Record inserted successfully...")

                                            except Exception as e:
                                                print(e)
                                                mysqldb.rollback()
                                                mysqldb.close()

                                            '''name = str(box1)
                                            mob = str(box6)
                                            date = str(box8)
                                            room = str(box11)
                                            amount = str(box13)
                                            msg = 'Hello ' + name + ' Welcome to hoteldatabase your Booking is successfully done on ' + date + ' and your Room No is ' + room + ' you paid amount is ' + amount + ' /- Rs have a nice day'
                                            url = "https://www.fast2sms.com/dev/bulk"
                                
                                            payload = "sender_id=CHKSMS&message=" + msg + "&language=english&route=p&numbers=" + mob + ""
                                            headers = {
                                                'authorization': "ftF4lGVr8jQaoYpLeCwEbIycnzkBTO6g95ARqiuhWPNvKZ1dSJP5Iithg4xAub16RTwWDpqkMHFacLJC",
                                                'Content-Type': "application/x-www-form-urlencoded",
                                                'Cache-Control': "no-cache",
                                            }
                                
                                            response = requests.request("POST", url, data=payload, headers=headers)
                                            print(response.text)'''
                                            print(box, box1, box2, box3, box4, box5, box6, box7, box8, box9, box10, box11, box12, box13)
                                            self.data.set("")
                                            self.data_1.set("")
                                            self.data_2.set("")
                                            self.data_3.set("")
                                            self.data_4.set("")
                                            self.data_5.set("")
                                            self.data_6.set("")
                                            self.data_7.set("")
                                            self.data_8.set("")
                                            self.data_9.set("")
                                            self.data_10.set("")
                                            self.data_11.set("")
                                            self.data_12.set("")
                                            self.data_13.set("")
                                            self.data_14.set("")
                                            self.data_15.set("")
                                            self.data_16.set("")

    def reset(self):
        self.data.set("")
        self.data_1.set("")
        self.data_2.set("")
        self.data_3.set("")
        self.data_4.set("")
        self.data_5.set("")
        self.data_6.set("")
        self.data_7.set("")
        self.data_8.set("")
        self.data_9.set("")
        self.data_10.set("")
        self.data_11.set("")
        self.data_12.set("")
        self.data_13.set("")
        self.data_14.set("")
        self.data_15.set("")
        self.data_16.set("")


    def Room_Num(self):
        temp = self.data_10.get()
        if temp == "Single bed":
            x = random.randint(200, 220)
            amount1 = 999
            self.data_11.set(x)
            self.data_13.set(amount1)
            Entry(self.details, textvariable=self.data_14, width=22, borderwidth=3, state='disable').place(x=10, y=530)
            Entry(self.details, textvariable=self.data_15, width=22, borderwidth=3, state='disable').place(x=160, y=530)
        elif temp == "Double bed":
            y = random.randint(221, 240)
            amount2 = 1999
            self.data_11.set(y)
            self.data_13.set(amount2)
            Entry(self.details, textvariable=self.data_14, width=22, borderwidth=3).place(x=10, y=530)
            Entry(self.details, textvariable=self.data_15, width=22, borderwidth=3, state='disable').place(x=160, y=530)
        elif temp == 'Triple bed':
            z = random.randint(241, 260)
            amount3 = 2999
            self.data_11.set(z)
            self.data_13.set(amount3)
            Entry(self.details, textvariable=self.data_14, width=22, borderwidth=3).place(x=10, y=530)
            Entry(self.details, textvariable=self.data_15, width=22, borderwidth=3).place(x=160, y=530)
        else:
            mgs.showinfo('Room', 'Room Type Not Selected')

    def check(self):
        temp_1 = self.data_8.get()
        #temp_2 = self.data_9.get()
        temp_3 = self.data_11.get()
        mysqldb = mysql.connector.connect(host="localhost", user="root", passwd="chitra", database="hotel")
        mycursor = mysqldb.cursor()
        try:
            mycursor.execute("SELECT*FROM customer_details where Room_Num='"+temp_3+"'")
            record = mycursor.fetchall()
            print(record)
        except Exception as e:
            print(e)
        for row in record:
            if temp_1 == row[8]:
                mgs.showinfo('Room', 'Room Already Booked')
                return 0
            elif temp_1 == row[9]:
                mgs.showinfo('Room', 'Room Already Booked')
                return 0
        else:
            mgs.showinfo('Room', 'Room Available')
    def reference_Num(self):
        y = random.randrange(1000, 50000)
        self.data.set(y)


    def statistic(self):
        mysqldb = mysql.connector.connect(host="localhost", user="root", passwd="", database="hotel")
        mycursor = mysqldb.cursor()
        mycursor.execute("select CheckIn from customer_details")
        record = mycursor.fetchall()
        print(record)
        Date = []
        Amount = []
        for row in record:
            Date.append(row[0])
        print(Date)
        mycursor.execute("select Amount from Customer_Details")
        record_2 = mycursor.fetchall()
        for ro in record_2:
            Amount.append(ro[0])
        print(Amount)
        book = xlsxwriter.Workbook('Book2.xlsx')
        outsheet = book.add_worksheet()
        outsheet.write("A1", "CheckIN ")
        outsheet.write("B1", "Amount")
        for item in range(len(Date)):
            outsheet.write(item + 1, 0, Date[item])
            outsheet.write(item + 1, 1, Amount[item])
        book.close()

        dataset = pd.read_excel('Book2.xlsx')
        dataset_profit = dataset.groupby('CheckIN').sum()['Amount'].reset_index()
        plt.plot(dataset_profit['CheckIN'], dataset_profit['Amount'], 'o-', color='Green')
        plt.ylim(0, 5000)
        plt.xticks(rotation='vertical')
        plt.xlabel('Dates')
        plt.ylabel('Amount')
        plt.show()

    def new_window(self):
        self.Search = Tk()
        self.Search.title("Sql Data")
        self.Search.geometry("1000x500")
        mysqldb = mysql.connector.connect(host="localhost", user="root", passwd="", database="hotel")
        mycursor = mysqldb.cursor()
        try:
            mycursor.execute("select*from Customer_Details")
        except Exception as e:
            print(e)


        tree = ttk.Treeview(self.Search, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), height=80)

        ver_scroll = ttk.Scrollbar(self.Search, orient="vertical")
        ver_scroll.configure(command=tree.yview)
        tree.configure(yscrollcommand=ver_scroll.set)
        ver_scroll.pack(fill=Y, side=RIGHT)

        hor_scroll = ttk.Scrollbar(self.Search, orient="horizontal")
        hor_scroll.configure(command=tree.xview)
        tree.configure(xscrollcommand=hor_scroll.set)
        hor_scroll.pack(fill=X, side=BOTTOM)
        tree.pack()
        tree["show"] = "headings"
        s = ttk.Style(self.Search)
        s.theme_use("clam")
        s.configure(".", font=("Helvectical", 10))
        s.configure("Treeview.Heading", foreground="Blue", font=("Helvectica", 10, "bold"))


        tree.column(1, width=100)
        tree.column(2, width=100)
        tree.column(3, width=100)
        tree.column(4, width=100)
        tree.column(5, width=100)
        tree.column(6, width=100)
        tree.column(7, width=100)
        tree.column(8, width=100)
        tree.column(9, width=100)
        tree.column(10, width=100)
        tree.column(11, width=100)
        tree.column(12, width=100)
        tree.column(13, width=100)
        tree.column(14, width=100)
        tree.column(15, width=100)
        tree.column(16, width=100)

        tree.heading(1, text="Ref Num")
        tree.heading(2, text="First Nam")
        tree.heading(3, text="Last Nam")
        tree.heading(4, text="Gender")
        tree.heading(5, text="Id Proof")
        tree.heading(6, text="Id Num")
        tree.heading(7, text="Mobile Num")
        tree.heading(8, text="Address")
        tree.heading(9, text="Checkin Date")
        tree.heading(10, text="Checkout Date")
        tree.heading(11, text="Room Type")
        tree.heading(12, text="Room Num")
        tree.heading(13, text="Payment Method")
        tree.heading(14, text="Amount")
        tree.heading(15, text="Person_1")
        tree.heading(16, text="Person_2")
        i = 0
        for ro in mycursor:
            tree.insert("", i, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10], ro[11], ro[12], ro[13], ro[14], ro[15]))
        self.Search.mainloop()

    def Search(self):
        BOX3 = self.data_16.get()
        mysqldb = mysql.connector.connect(host="localhost", user="root", passwd="", database="hotel")
        mycursor = mysqldb.cursor()
        if BOX3 == "":
            mgs.showinfo('Alert!', 'Search is missing')
        else:
            try:
                mycursor.execute("select firstname from customer_details")
                record = mycursor.fetchall()
                print(record)
                for ro in record:
                    if ro[0] == BOX3:
                        print('founded', ro[0])
                        try:
                            mycursor.execute("SELECT * from customer_details  WHERE firstname='" + ro[0] + "'")
                            self.Search = Tk()
                            self.Search.title('Search')
                            self.Search.geometry("1000x100")

                            tree = ttk.Treeview(self.Search,
                                                columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16),
                                                height=5)

                            ver_scroll = ttk.Scrollbar(self.Search, orient="vertical")
                            ver_scroll.configure(command=tree.yview)
                            tree.configure(yscrollcommand=ver_scroll.set)
                            ver_scroll.pack(fill=Y, side=RIGHT)

                            hor_scroll = ttk.Scrollbar(self.Search, orient="horizontal")
                            hor_scroll.configure(command=tree.xview)
                            tree.configure(xscrollcommand=hor_scroll.set)
                            hor_scroll.pack(fill=X, side=BOTTOM)
                            tree.pack()
                            tree["show"] = "headings"
                            s = ttk.Style(self.Search)
                            s.theme_use("clam")
                            s.configure(".", font=("Helvectical", 10))
                            s.configure("Treeview.Heading", foreground="Blue", font=("Helvectica", 10, "bold"))

                            tree.column(1, width=100)
                            tree.column(2, width=100)
                            tree.column(3, width=100)
                            tree.column(4, width=100)
                            tree.column(5, width=100)
                            tree.column(6, width=100)
                            tree.column(7, width=100)
                            tree.column(8, width=100)
                            tree.column(9, width=100)
                            tree.column(10, width=100)
                            tree.column(11, width=100)
                            tree.column(12, width=100)
                            tree.column(13, width=100)
                            tree.column(14, width=100)
                            tree.column(15, width=100)
                            tree.column(16, width=100)

                            tree.heading(1, text="Ref Num")
                            tree.heading(2, text="First Nam")
                            tree.heading(3, text="Last Nam")
                            tree.heading(4, text="Gender")
                            tree.heading(5, text="Id Proof")
                            tree.heading(6, text="Id Num")
                            tree.heading(7, text="Mobile Num")
                            tree.heading(8, text="Address")
                            tree.heading(9, text="Checkin Date")
                            tree.heading(10, text="Checkout Date")
                            tree.heading(11, text="Room Type")
                            tree.heading(12, text="Room Num")
                            tree.heading(13, text="Payment Method")
                            tree.heading(14, text="Amount")
                            tree.heading(15, text="Person_1")
                            tree.heading(16, text="Person_2")
                            i = 0
                            for ro in mycursor:
                                tree.insert("", i, values=(
                                    ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10],
                                    ro[11],
                                    ro[12], ro[13], ro[14], ro[15]))
                            self.data_16.set("")
                            self.Search.mainloop()
                        except Exception as e:
                            print(e)

                        return 0
                else:
                    mgs.showinfo('Alert!', 'Record Not Found')
            except Exception as e:
                print(e)

    def add_frame2(self):
        self.details = Tk()
        self.details.title("Hotel_Management_System")
        self.details.geometry("500x750")
        self.details.configure(background='#8DEEEE')

        self.data = StringVar()
        self.data_1 = StringVar()
        self.data_2 = StringVar()
        self.data_3 = StringVar()
        self.data_4 = StringVar()
        self.data_5 = StringVar()
        self.data_6 = StringVar()
        self.data_7 = StringVar()
        self.data_8 = StringVar()
        self.data_9 = StringVar()
        self.data_10 = StringVar()
        self.data_11 = StringVar()
        self.data_12 = StringVar()
        self.data_13 = StringVar()
        self.data_14 = StringVar()
        self.data_15 = StringVar()
        self.data_16 = StringVar()
        #self.data_17 = StringVar()

        Label(self.details, text="Customer Details", font=200, fg="Blue", bg='#8DEEEE').place(x=10, y=10)

        Label(self.details, text="Reference No.", font=80, bg='#8DEEEE').place(x=10, y=50)
        Entry(self.details, textvariable=self.data, width=22, borderwidth=3).place(x=10, y=80)
        Button(self.details, text="Allocate", command=self.reference_Num, width=10).place(x=10, y=110)

        Label(self.details, text="First Name", font=80, anchor=SW, bg='#8DEEEE').place(x=160, y=50)
        Entry(self.details, textvariable=self.data_1, width=22, borderwidth=3).place(x=160, y=80)

        Label(self.details, text="Last Name", font=80, anchor=SW, bg='#8DEEEE').place(x=310, y=50)
        Entry(self.details, textvariable=self.data_2, width=22, borderwidth=3).place(x=310, y=80)

        Label(self.details, text="Gender", font=80, anchor=SW, bg='#8DEEEE').place(x=10, y=150)
        combo_gender = tkinter.ttk.Combobox(self.details, textvariable=self.data_3, width=19)
        combo_gender["value"] = ["Male", "Female", "Other"]
        combo_gender.place(x=10, y=180)

        Label(self.details, text="ID Proof", font=80, anchor=SW, bg='#8DEEEE').place(x=160, y=150)
        combo_proof = ttk.Combobox(self.details, textvariable=self.data_4, width=19)
        combo_proof["value"] = ["Aadhaar", "Driving card", "Voter Id", "Passport"]
        combo_proof.place(x=160, y=180)

        Label(self.details, text="ID No.", font=80, anchor=SW, bg='#8DEEEE').place(x=310, y=150)
        Entry(self.details, textvariable=self.data_5, width=22, borderwidth=3).place(x=310, y=180)

        Label(self.details, text="Mobile No.", font=80, anchor=SW, bg='#8DEEEE').place(x=10, y=220)
        Entry(self.details, textvariable=self.data_6, width=22, borderwidth=3).place(x=10, y=250)

        Label(self.details, text="Address", font=80, anchor=SW, bg='#8DEEEE').place(x=160, y=220)
        Entry(self.details, textvariable=self.data_7, width=22, borderwidth=3).place(x=160, y=250)

        Label(self.details, text="Checkin date", font=80, anchor=SW, bg='#8DEEEE').place(x=10, y=290)
        DateEntry(self.details, textvariable=self.data_8, width=19, borderwidth=3).place(x=10, y=320)

        Label(self.details, text="Checkout date", font=80, anchor=SW, bg='#8DEEEE').place(x=160, y=290)
        DateEntry(self.details, textvariable=self.data_9, width=19).place(x=160, y=320)

        Label(self.details, text="Room Type", font=80, anchor=SW, bg='#8DEEEE').place(x=10, y=360)
        combo_proof = ttk.Combobox(self.details, textvariable=self.data_10, width=19)
        combo_proof["value"] = ["Single bed", "Double bed", "Triple bed"]
        combo_proof.place(x=10, y=390)

        Label(self.details, text="Room No.", font=80, anchor=SW, bg='#8DEEEE').place(x=160, y=360)
        Entry(self.details, textvariable=self.data_11, width=22, borderwidth=3).place(x=160, y=390)
        Button(self.details, text="Allocate", width=10, command=self.Room_Num).place(x=310, y=390)
        Button(self.details, text="Check", width=10, command=self.check).place(x=410, y=390)

        Label(self.details, text="Payment Method", font=80, anchor=SW, bg='#8DEEEE').place(x=10, y=430)
        combo_proof = ttk.Combobox(self.details, textvariable=self.data_12, width=19)
        combo_proof["value"] = ["Cash", "Online banking", "Debit Card", "Credit Card"]
        combo_proof.place(x=10, y=460)

        Label(self.details, text="Amount", font=80, anchor=SW, bg='#8DEEEE').place(x=160, y=430)
        Entry(self.details, textvariable=self.data_13, width=22, borderwidth=3).place(x=160, y=460)

        Label(self.details, text="Person name 1", font=80, anchor=SW, bg='#8DEEEE').place(x=10, y=500)
        Entry(self.details, textvariable=self.data_14, width=22, borderwidth=3, state='disable').place(x=10, y=530)

        Label(self.details, text="Person name 2", font=80, anchor=SW, bg='#8DEEEE').place(x=160, y=500)
        Entry(self.details, textvariable=self.data_15, width=22, borderwidth=3, state='disable').place(x=160, y=530)

        Button(self.details, text="reset", command=self.reset, width=10, fg="Red", font=80, borderwidth=3).place(x=10, y=580)

        Button(self.details, text="Book-Now", command=self.insert_data, width=20, fg="Green", font=80, borderwidth=3).place(x=160, y=580)

        Button(self.details, text="Bookings", command=self.new_window, width=10, fg="#FF6103", font=80, borderwidth=3).place(x=10, y=630)

        Button(self.details, text="Profit", command=self.statistic, width=10, fg="#B23AEE", font=80, borderwidth=3).place(x=160, y=630)

        Label(self.details, text="Search", font=80, anchor=SW, bg='#8DEEEE').place(x=10, y=700)
        Entry(self.details, textvariable=self.data_16, width=22, borderwidth=3).place(x=100, y=700)
        Button(self.details, text="Ok", width=10, command=self.Search).place(x=250, y=700)

        self.details.resizable(False, False)
        self.details.mainloop()

