from tkinter import messagebox
import sqlite3
def create():
    con = sqlite3.connect("master.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS account(id INTEGER PRIMARY KEY,user TEXT, password TEXT)")
    #cur.execute("CREATE TABLE IF NOT EXISTS stock(id INTEGER PRIMARY KEY,idly1 INTEGER, dosa1 INTEGER, kesari1 INTEGER, drinks1 INTEGER, pulav1 INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS stocky(id INTEGER PRIMARY KEY,idly1 TEXT, dosa1 TEXT, kesari1 TEXT, drinks1 TEXT, pulav1 TEXT)")
    con.commit()
    con.close()
def viewall():
    con = sqlite3.connect("master.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account")
    rows = cur.fetchall()
    con.close()
    return rows
def viewstock():
    con = sqlite3.connect("master.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM stocky where id=1")
    rows = cur.fetchall()
    con.close()
    return rows

def search(user="",password=""):
    con = sqlite3.connect("master.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account WHERE user=? AND password=?",(user,password))
    rows = cur.fetchall()
    con.close()
    return rows
def update(id,a1,a2,a3,a4,a5):
    con = sqlite3.connect("master.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM stocky where id=1")
    rows = cur.fetchall()
    if not rows:
            a=0
            b=0
            c=0
            d=0
            e=0
    else:
            a=int(a1)+int(rows[0][1])
            b=int(a2)+int(rows[0][2])
            c=int(a3)+int(rows[0][3])
            d=int(a4)+int(rows[0][4])
            e=int(a5)+int(rows[0][5])
    
    cur.execute("UPDATE stocky SET idly1=?,dosa1=?,kesari1=?,drinks1=?,pulav1=? WHERE id=?",(a,b,c,d,e,id))
    con.commit()
    con.close()
    messagebox.showinfo('Admin','Record Updated Successfully')
    return

def updateB(id,a1,a2,a3,a4,a5):
    if (a1==""):
            a1="0"
    if (a2==""):
            a2="0"
    if (a3==""):
            a3="0"
    if (a4==""):
            a4="0"
    if (a5==""):
            a5="0"


    con = sqlite3.connect("master.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM stocky where id=1")
    rows = cur.fetchall()
    if not rows:
            a=0
            b=0
            c=0
            d=0
            e=0
    else:
            a=int(rows[0][1])-int(a1)
            b=int(rows[0][2])-int(a2)
            c=int(rows[0][3])-int(a3)
            d=int(rows[0][4])-int(a4)
            e=int(rows[0][5])-int(a5)
    
    cur.execute("UPDATE stocky SET idly1=?,dosa1=?,kesari1=?,drinks1=?,pulav1=? WHERE id=?",(a,b,c,d,e,id))
    con.commit()
    con.close()
    return    
    
def add(user,password):
    con = sqlite3.connect("master.db")
    cur = con.cursor()
    cur.execute("INSERT INTO account VALUES(NULL,?,?)",(user,password))
    con.commit()
    con.close()
def add1():
    con = sqlite3.connect("master.db")
    cur = con.cursor()
    cur.execute("INSERT INTO stocky VALUES(NULL,'10','10','10','10','10')")
    con.commit()
    con.close()
    messagebox.showinfo('Admin','Record Added Successfully')
def delete(user):
    con = sqlite3.connect("master.db")
    cur = con.cursor()
    cur.execute("DELETE FROM account WHERE user=?",(user,))
    con.commit()
    con.close()
    messagebox.showinfo('Admin','Record Deleted Successfully')
create()
#print(search(category="social"))
