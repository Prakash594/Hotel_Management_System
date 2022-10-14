import subprocess as sp
import matplotlib.pyplot as plt
import pandas as pd
import re
re.match("^[A-Z,a-z]*$")
import xlsxwriter
import openpyxl
import mysql.connector
'''name = 'Vasant'
last = 'Jayaraman'
Checkin = '5/5/2021'
Checkout = '5/6/2021'
RoomType = 'Single'
RoomNum = '206'
Amount = '900'
f = open('test.txt', 'w')
f.write('      Welcome to Hotel Database \n'
        '================Bill=================\n'
        'Name:                '+name+' '+last+'\n'
        'CheckIn Date:          '+Checkin+'\n'       
        'CheckOut Date:         '+Checkout+'\n'
        'Room Type:             '+RoomType+'\n'
        'Room No.:              '+RoomNum+'\n'
        'Amount:                '+Amount+'\n')
f.close()
f2 = open('test.txt', 'a')
f2.close()'''
#f.write('Hello')
'''mysqldb = mysql.connector.connect(host="localhost", user="root", passwd="chitra", database="hotel")
mycursor = mysqldb.cursor()
mycursor.execute("select CheckIN from Customer_Details")
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
outsheet.write("A1", "CheckIN")
outsheet.write("B1", "Amount")
for item in range(len(Date)):
    outsheet.write(item+1, 0, Date[item])
    outsheet.write(item+1, 1, Amount[item])
book.close()'''
dataset = pd.read_csv('D:\sqlDatabase\Book1.csv')
plt.plot(dataset.CheckIN, dataset.Amount, '-o')
plt.ylim(0, 5000)
plt.xlabel('Dates')
plt.ylabel('Amount')
plt.show()
