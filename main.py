# tkinter
import sqlite3

from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3

conn = sqlite3.connect('3005Proj.db')
cursor = conn.cursor()
my_w = tk.Tk()
my_w.geometry("1000x600")
tv = ttk.Treeview(my_w, columns=(1, 2, 3, 4, 5, 6), show="headings", height="10")
tv.place(x=0, y=250)
tv.winfo_geometry()
my_w.title("3005 Project: University Bookstore, by Max Curkovic")

title_label = Label(my_w, text = "University Bookstore: COMP 3005 Project", relief=RAISED, font=("Arial", 20))
title_label.pack()

author_label = Label(my_w, text = "Max Curkovic, 101139937", relief=RAISED, font=("Arial", 12))
author_label.pack()

def clear_table():
    for col in tv['columns']:
        tv.heading(col, text='')
    tv.delete(*tv.get_children())

def userButton():
    clear_table()
    cursor.execute("SELECT * from user")
    rows = cursor.fetchall()
    tv.column(1, anchor=CENTER, stretch=NO, width=100)
    tv.heading(1, text="UserID")
    tv.column(2, anchor=CENTER, stretch=NO, width=225)
    tv.heading(2, text="Email")
    tv.column(3, anchor=CENTER, stretch=NO, width=125)
    tv.heading(3, text="Password")
    for i in rows:
        tv.insert('', 'end', values=i)

def textbookButton():
    clear_table()
    cursor.execute("SELECT * from textbook")
    rows = cursor.fetchall()
    tv.column(1, anchor=CENTER, stretch=NO, width=100)
    tv.heading(1, text="TextbookCode")
    tv.column(2, anchor=CENTER, stretch=NO, width=125)
    tv.heading(2, text="Stock")
    tv.column(3, anchor=CENTER, stretch=NO, width=125)
    tv.heading(3, text="Price")
    tv.column(4, anchor=CENTER, stretch=NO, width=200)
    tv.heading(4, text="Title")
    tv.column(5, anchor=CENTER, stretch=NO, width=125)
    tv.heading(5, text="Author")
    tv.column(6, anchor=CENTER, stretch=NO, width=125)
    tv.heading(6, text="Type Course")
    for i in rows:
        tv.insert('', 'end', values=i)

def suppliesButton():
    clear_table()
    cursor.execute("SELECT * from supplies")
    rows = cursor.fetchall()
    tv.column(1, anchor=CENTER, stretch=NO, width=100)
    tv.heading(1, text="SupplyID")
    tv.column(2, anchor=CENTER, stretch=NO, width=225)
    tv.heading(2, text="Supply Name")
    tv.column(3, anchor=CENTER, stretch=NO, width=125)
    tv.heading(3, text="Stock")
    tv.column(4, anchor=CENTER, stretch=NO, width=125)
    tv.heading(4, text="Price")
    tv.column(5, anchor=CENTER, stretch=NO, width=125)
    tv.heading(5, text="Type of Supply")
    for i in rows:
        tv.insert('', 'end', values=i)

def userSuppliesButton():
    clear_table()
    cursor.execute("SELECT * from user_supplies")
    rows = cursor.fetchall()
    tv.column(1, anchor=CENTER, stretch=NO, width=100)
    tv.heading(1, text="UserID")
    tv.column(2, anchor=CENTER, stretch=NO, width=225)
    tv.heading(2, text="SupplyID")
    for i in rows:
        tv.insert('', 'end', values=i)

def userTextbooksButton():
    clear_table()
    cursor.execute("SELECT * from user_textbook")
    rows = cursor.fetchall()
    tv.column(1, anchor=CENTER, stretch=NO, width=100)
    tv.heading(1, text="UserID")
    tv.column(2, anchor=CENTER, stretch=NO, width=225)
    tv.heading(2, text="Textbook Code")
    for i in rows:
        tv.insert('', 'end', values=i)

def orderButton():
    clear_table()
    cursor.execute("SELECT * from user_order")
    rows = cursor.fetchall()
    tv.column(1, anchor=CENTER, stretch=NO, width=100)
    tv.heading(1, text="OrderID")
    tv.column(2, anchor=CENTER, stretch=NO, width=225)
    tv.heading(2, text="UserID")
    tv.column(3, anchor=CENTER, stretch=NO, width=100)
    tv.heading(3, text="Textbook Code")
    tv.column(4, anchor=CENTER, stretch=NO, width=100)
    tv.heading(4, text="SupplyID")
    for i in rows:
        tv.insert('', 'end', values=i)


def clickQuery1Button():
    clear_table()
    cursor.execute("SELECT * from supplies where type_supply='writing'");
    rows = cursor.fetchall()
    tv.column(1, anchor=CENTER, stretch=NO, width=100)
    tv.heading(1, text="SupplyID")
    tv.column(2, anchor=CENTER, stretch=NO, width=225)
    tv.heading(2, text="Supply Name")
    tv.column(3, anchor=CENTER, stretch=NO, width=125)
    tv.heading(3, text="Stock")
    tv.column(4, anchor=CENTER, stretch=NO, width=125)
    tv.heading(4, text="Price")
    tv.column(5, anchor=CENTER, stretch=NO, width=125)
    tv.heading(5, text="Type of Supply")
    for i in rows:
        tv.insert('', 'end', values=i)

def clickQuery2Button():
    clear_table()
    cursor.execute("SELECT * from textbook where type_course='CHEM'");
    rows = cursor.fetchall()
    tv.column(1, anchor=CENTER, stretch=NO, width=100)
    tv.heading(1, text="TextbookCode")
    tv.column(2, anchor=CENTER, stretch=NO, width=125)
    tv.heading(2, text="Stock")
    tv.column(3, anchor=CENTER, stretch=NO, width=125)
    tv.heading(3, text="Price")
    tv.column(4, anchor=CENTER, stretch=NO, width=200)
    tv.heading(4, text="Title")
    tv.column(5, anchor=CENTER, stretch=NO, width=125)
    tv.heading(5, text="Author")
    tv.column(6, anchor=CENTER, stretch=NO, width=125)
    tv.heading(6, text="Type Course")
    for i in rows:
        tv.insert('', 'end', values=i)

def clickQuery3Button():
    clear_table()
    cursor.execute("SELECT user_id, textbook_code, title from user_textbook NATURAL JOIN textbook where user_id=1001")
    rows = cursor.fetchall()
    tv.column(1, anchor=CENTER, stretch=NO, width=100)
    tv.heading(1, text="UserID")
    tv.column(2, anchor=CENTER, stretch=NO, width=225)
    tv.heading(2, text="Textbook Code")
    tv.column(3, anchor=CENTER, stretch=NO, width=125)
    tv.heading(3, text="Title")
    for i in rows:
        tv.insert('', 'end', values=i)

def clickQuery4Button():
    clear_table()
    cursor.execute("SELECT author from textbook where stock<=5 and type_course='ECOR'");
    rows = cursor.fetchall()
    tv.column(1, anchor=CENTER, stretch=NO, width=100)
    tv.heading(1, text="Author")
    for i in rows:
        tv.insert('', 'end', values=i)

usersButton = Button(my_w, text="All Users", command=userButton)
usersButton.place(x=600, y=100)
textbooksButton = Button(my_w, text="All Textbooks", command=textbookButton)
textbooksButton.place(x=655, y=100)
suppliesButton = Button(my_w, text="All Supplies", command=suppliesButton)
suppliesButton.place(x=600, y=125)
ordersButton = Button(my_w, text="All Orders", command=orderButton)
ordersButton.place(x=671, y=125)
userTextbooksButton = Button(my_w, text="User Textbooks", command=userTextbooksButton)
userTextbooksButton.place(x=678, y=150)
userSuppliesButton = Button(my_w, text="User Supplies", command=userSuppliesButton)
userSuppliesButton.place(x=600, y=150)
query1Button = Button(my_w, text="Query #1: Supplies with type 'writing'", command=clickQuery1Button)
query1Button.place(x=0, y=100)
query2Button = Button(my_w, text="Query #2: Textbooks with type 'CHEM'", command=clickQuery2Button)
query2Button.place(x=0, y=125)
query3Button = Button(my_w, text="Query #3: Textbooks that user 1001 has added to system", command=clickQuery3Button)
query3Button.place(x=0, y=150)
query4Button = Button(my_w, text="Query #4: Textbook authors with type 'ECOR' and less than 5 stock", command=clickQuery4Button)
query4Button.place(x=0, y=175)

my_w.mainloop()