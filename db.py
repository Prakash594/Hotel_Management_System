import mysql.connector
from tkinter import *
import tkinter.ttk
def user_login(tup):
    mysqldb = mysql.connector.connect(host="localhost", user="root", passwd="", database="hotel")
    mycursor = mysqldb.cursor()
    try:
        mycursor.execute("SELECT * FROM `username_password` WHERE `username`=%s AND `passwd`=%s", tup)
        return (mycursor.fetchone())
    except:
        return False

def admin_Login(tup):
    mysqldb = mysql.connector.connect(host="localhost", user="root", passwd="", database="hotel")
    mycursor = mysqldb.cursor()
    try:
        mycursor.execute("SELECT * FROM `admin_password` WHERE `admin_username`=%s AND `admin_passwd`=%s", tup)
        return (mycursor.fetchone())
    except:
        return False



