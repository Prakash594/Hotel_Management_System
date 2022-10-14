from tkinter import *
from tkinter import messagebox as mgs
from Admin_Manage import Admin
import db
from PIL import ImageTk, Image

class Login:
    def __init__(self, log):
        self.log = log
        self.log.title("Admin Login")
        self.log.geometry("350x200")
        self.log.configure(background='#CAFF70')

        #mysqldb = mysql.connector.connect(host="localhost", user="root", passwd="chitra", database="hotel")
        #mycursor = mysqldb.cursor()
    def add_frame(self):
        self.data_15 = StringVar()
        self.data_16 = StringVar()
        mypic = Image.open('loginperson.jpg')
        resized = mypic.resize((150, 143), Image.ANTIALIAS)
        myimg = ImageTk.PhotoImage(resized)
        Label(self.log, image=myimg, width=100, height=120).place(x=10, y=10)
        Label(self.log, text='Username', font=100, bg='#CAFF70').place(x=120, y=20)
        Entry(self.log, textvariable=self.data_15, width=20).place(x=220, y=20)

        Label(self.log, text='Security key', font=100, bg='#CAFF70').place(x=120, y=60)
        Entry(self.log, textvariable=self.data_16, width=20, show='*').place(x=220, y=60)

        Button(self.log, text="Reset", command=self.Reset_2, width=8, fg="Red", font=50, borderwidth=3).place(x=120,
                                                                                                              y=100)
        Button(self.log, text="Login", command=self.newframe, width=8, fg="#B23AEE", font=50, borderwidth=3).place(
            x=220, y=100)

        self.log.resizable(False, False)
        self.log.mainloop()
    def Reset_2(self):
        self.data_15.set("")
        self.data_16.set("")

    def newframe(self):
        box15 = self.data_15.get()
        box16 = self.data_16.get()
        data = (box15, box16)
        if self.data_15.get() == "":
            mgs.showinfo("Alert!", "Enter Username")
        elif self.data_16.get() == "":
            mgs.showinfo("Alert!", "Enter Security Key")
        else:
            res2 = db.admin_Login(data)

            if res2:
                mgs.showinfo("Message", "Login Successfully")
                log.destroy()
                y = Admin()
                y.add_frame2()
            else:
                mgs.showinfo("ALert!", "Wrong username/password")

if __name__ == "__main__":
    log = Tk()
    x = Login(log)
    x.add_frame()