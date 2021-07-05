'''                    
                        Experiment -15
# Program code by Kshitij.(Remove this line while submitting)

Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------

Topic- GUI Tkinter in Python
AIM- Write a program to create a GUI application using Tkinter and connect to Database.
'''

from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

is_on = True


def switch():
    global is_on
    if is_on:
        t2.config(image=off)

        is_on = False
    else:

        t2.config(image=on)
        is_on = True


def View():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    if numt.get() == "ALL Years":
        if is_on:
            cur.execute("SELECT * FROM studentdetails order by sname DESC ")
        else:
            cur.execute("SELECT * FROM studentdetails ")
        rows = cur.fetchall()
        for row in rows:
            print(row)
            tree.insert("", END, values=row)
    else:
        if is_on:
            cur.execute("SELECT * FROM studentdetails where year = ? order by sname DESC ", (numt.get(),))
        else:
            cur.execute("SELECT * FROM studentdetails where year = ? ", (numt.get(),))
        rows = cur.fetchall()
        for row in rows:
            print(row)
            tree.insert("", END, values=row)

    conn.close()


conn = sqlite3.connect('student.db')

cur = conn.cursor()
master = Tk()
master.geometry("1150x400")
master.title("Student Form")

l = Label(master, text="Student Details Entry Form")
l1 = Label(master, text="Student ID")
l2 = Label(master, text="Student Name")
l3 = Label(master, text="Division")
l4 = Label(master, text="Year")

num1 = Entry(master)
num2 = Entry(master)
num3 = Entry(master)
num4 = StringVar()
numt = StringVar()

options = [
    "First year",
    "Second year",
    "Third year",
    "Final Year"
]

l.place(x=50, y=5)
l1.place(x=10, y=40)
num1.place(x=100, y=40)
l2.place(x=10, y=80)
num2.place(x=100, y=80)
l3.place(x=10, y=120)
num3.place(x=100, y=120)
l4.place(x=10, y=160)
num4.set("First year")
drop = OptionMenu(master, num4, *options)
drop.place(x=100, y=160)

tree = ttk.Treeview(master, column=("column1", "column2", "column3", 'column4'), show='headings')
tree.heading("#1", text="Student Id")
tree.heading("#2", text="Student Name")
tree.heading("#3", text="Division")
tree.heading("#4", text="Year")
tree.place(x=300, y=20)

t1 = Button(text="view data", command=View)
t1.place(x=500, y=270)

# Define Our Images
on = ImageTk.PhotoImage(Image.open('on.png').resize((30, 15), Image.ANTIALIAS))
off = ImageTk.PhotoImage(Image.open('off.png').resize((30, 15), Image.ANTIALIAS))

l4 = Label(master, text="Sort Descending")
l4.place(x=500, y=320)

t2 = Button(text="view data", image=on, command=switch)
t2.place(x=600, y=320)

numt.set("First year")
dropt = OptionMenu(master, numt, *options, "ALL Years")
dropt.place(x=700, y=270)


def update():
    if cur.execute('select * from studentdetails where sid=?', (num1.get(),)).fetchone() is not None:
        cur.execute(
            "UPDATE studentdetails SET sname = ?, div = ?, year = ? where sid = ?",
            (num2.get(), num3.get(), num4.get(), num1.get()))
        conn.commit()
    else:
        print("not exists")


def reg():
    print('sucessful', num1.get(), num2.get(), num3.get(), num3.get())
    st = cur.execute("INSERT INTO studentdetails VALUES(?,?,?,?)", (num1.get(), num2.get(), num3.get(), num4.get()))
    conn.commit()


def sear():
    print('hello')
    try:
        res1 = cur.execute('select * from studentdetails where sid=?', (num1.get(),))
        co = res1.fetchone()
        if co is not None:
            print(co)
            num1.delete(0, END)
            num2.delete(0, END)
            num3.delete(0, END)
            num1.insert(0, co[0])
            num2.insert(0, co[1])
            num3.insert(0, co[2])
            num4.set(co[3])
        else:
            messagebox.showinfo("Message", "No Record Exist Check Student Id")
            num1.delete(0, END)
    except:
        print('error')


def delete():
    try:
        if cur.execute("select * from studentdetails where sid=?", (num1.get(),)).fetchone() is not None:
            cur.execute("delete from studentdetails where sid=?", (num1.get(),))
            conn.commit()
            num1.delete(0, END)
            num2.delete(0, END)
            num3.delete(0, END)
            messagebox.showinfo("Message", "deleted successfully")
        else:
            messagebox.showinfo("Message", "No Record Exist Check Student Id")
            num1.delete(0, END)
    except EXCEPTION as e:
        messagebox.showinfo("Message", e)


b1 = Button(master, text="Register", command=reg)
b1.place(x=40, y=200)
b2 = Button(master, text="Quit", command=master.destroy)
b2.place(x=110, y=200)
b3 = Button(master, text="Search", command=sear)
b3.place(x=160, y=200)
b4 = Button(master, text="Delete", command=delete)
b4.place(x=60, y=240)
b5 = Button(master, text="Update", command=update)
b5.place(x=120, y=240)

master.mainloop()
