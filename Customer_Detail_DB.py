
import tkinter as tk
from tkinter import *

import tkinter.messagebox as MessageBox
import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="admin123",database="sample3",auth_plugin="mysql_native_password")
cursor=conn.cursor()

def showTables():
    pass

def TableExist():

    TableName=entExist.get()
    cursor.execute("SHOW TABLES")
    res=cursor.fetchall()
    if not res:
        cursor.execute("CREATE TABLE " + TableName + "(Id INT PRIMARY KEY, Name varchar(200), Phone BIGINT )")
        MessageBox.showinfo("Table", "Table Created")
        cursor.execute("commit")

    else:

        MessageBox.showinfo(TableName, "Table is Already Exist")
        cursor.execute("commit")

def Insert():

    Id = entId.get()
    Name = entName.get()
    Phone = entPhone.get()
    TableName = entExist.get()

    if (Id=="" or Name=="" or Phone==""):
        MessageBox.showerror("Feilds","Feilds Required")

    else:

        cursor.execute(f"insert into {TableName} values ('"+ Id +"','"+ Name +"','"+ Phone +"')")

        cursor.execute("commit")

        MessageBox.showinfo("Insert Details", "Inserted Successfully")
        conn.close()


def DeleteTable():
    l=[]
    cursor.execute("SHOW TABLES")
    ans=cursor.fetchall()
    for i in range(len(ans)):
        l.append(*ans[i])
        for j in range(len(l)):
            cursor.execute("DROP TABLE " + l.pop(j))
            MessageBox.showinfo("DROP TABLE","TABLE DELETE")

# SO HEHE WHAT CAN I DO LIKE USE TREEVIEW FOR SHOW TABLES FOR INSERT DATA AND SHOW RECODRS,USE IF ELSE


win=Tk()

frm1=Frame(win)
frm1.pack()


Id=StringVar()
Name=StringVar()
Phone=StringVar()
Not_Exist=StringVar()

lblhead=Label(frm1,text="Table",font=('Arial',20))
lblhead.grid(row=0,column=1,columnspan=3,pady=10)

label1=Label(frm1,text="TableExist")
label1.grid(row=1,column=1,sticky=W)

entExist=Entry(frm1,textvariable=Not_Exist)
entExist.grid(row=1,column=2,sticky=N)

lblhead1=Label(frm1,text="Customer Detail",font=('Arial',20))
lblhead1.grid(row=2,column=1,columnspan=3,pady=10,sticky=N)

label2=Label(frm1,text="Enter Id")
label2.grid(row=3,column=1,sticky=W)

entId=Entry(frm1,textvariable=Id)
entId.grid(row=3,column=2)

label3=Label(frm1,text="Enter Name")
label3.grid(row=4,column=1,sticky=W)

entName=Entry(frm1,textvariable=Name)
entName.grid(row=4,column=2)

label4=Label(frm1,text="Enter Phone")
label4.grid(row=5,column=1,sticky=W)

entPhone=Entry(frm1,textvariable=Phone)
entPhone.grid(row=5,column=2)


btn=Button(frm1,text="Insert",command=Insert)
btn.grid(pady=10,row=6,column=1)


win.title("Customer Form")
win.geometry("400x400")
win.resizable(False,False)

bt_TableExist=Button(frm1,text="TableExist",command=TableExist)
bt_TableExist.grid(pady=10,row=6,column=2)

btndelete=Button(frm1,text="DeleteTable",command=DeleteTable)
btndelete.grid(pady=10,row=6,column=3)

win.mainloop()
