import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="admin123",database="sample3",auth_plugin="mysql_native_password")
cursor=mydb.cursor()

def addcustomer():
    cname, age, email=entName.get(), entAge.get(), entEmail.get()
    try:
        int(age)
    except ValueError:
        print(ValueError)
        errorLbl.config(text="You Entered Wrong Age")


    sql="INSERT INTO customers VALUES(%s, %s, %s)"
    cursor.execute(sql,(cname,age,email)) #so here we used the entry variables,
    mydb.commit()
    print("successful")
    return True

win=Tk()

frm1=Frame(win)
frm1.pack(side=tk.LEFT, padx=20)
# here i can also use label textvaribles to get name, age,email before this we have to make a stringvar
cname=StringVar()
age=StringVar()
email=StringVar()

lblhead=Label(frm1,text="Customer Detail",font=('Arial',25))
lblhead.grid(row=0,column=1,columnspan=3)

label1=Label(frm1,text="Name:")
label1.grid(row=1,column=1)

entName=Entry(frm1,textvariable=cname)
entName.grid(row=1,column=2)

label2=Label(frm1,text="Age")
label2.grid(row=2,column=1)

entAge=Entry(frm1,textvariable=age)
entAge.grid(row=2,column=2)

label3=Label(frm1,text="Email")
label3.grid(row=3,column=1)

entEmail=Entry(frm1,textvariable=email)
entEmail.grid(row=3,column=2)

btn=Button(frm1,text="Add Customer",command=addcustomer)
btn.grid(pady=10,row=4,column=2)

errorLbl=Label(frm1,text='')
errorLbl.grid(row=5,column=1)

win.title("Customer Form")
win.geometry("350x350")
win.resizable(False,False)
win.mainloop()
