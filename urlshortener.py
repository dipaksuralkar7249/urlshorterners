import math
import re
import mysql.connector as my
import tkinter as tk
import pyshorteners as py

mydb = my.connect(host="localhost",
                  user = "root",
                  password = "Dipak@123",
                  database= "urldatabase")
mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE TABLE url (new_url VARCHAR(255), old_url VARCHAR(255))")
    print("Table is created")
except Exception:
    print("Tabel is already Exists")

root = tk.Tk()
root.title("Url Shortener Project")
root.geometry("500x400")
root.configure(bg="lightblue")
shortener = py.Shortener()


def pri():
    url = entry1.get()
    # url is raw url
    short1 = shortener.tinyurl.short(url)
    # short1 is short url output
    entry2.insert(0, short1)
    sql1 = "INSERT INTO url (new_url, old_url) VALUES (%s, %s)"
    val = (short1,url)
    mycursor.execute(sql1,val)
    mydb.commit()
    print("Record is stored...")

def clear_entry():
    #clear entry widget after clear button clicked.
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')


label = tk.Label(root, text="Enter the URL", width=100, bg="lightblue", font=("Times New Roman", 15))
label.pack(pady=5, padx=10)

entry1 = tk.Entry(root, width=40, font=("Arial", 15))
entry1.pack(pady=5, padx=10)

b = tk.Button(root, text="Converts", width=20, height=1, command=pri, font=("Times New Roman", 15))
b.pack(pady=5, padx=10)

entry2 = tk.Entry(root, width=40, font=("Arial", 15))
entry2.pack(pady=5, padx=10)

clear = tk.Button(root, text="Clear", width=20, height=0, font=("Times New Roman", 15), command=clear_entry)
clear.pack(pady=5, padx=10)

root.mainloop()
