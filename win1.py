from tkinter import*
from tkinter import messagebox
import random
import time
import win1_bk


root=Tk()
root.geometry("1000x600+0+0")
root.title("My Restaurant")

Tops = Frame(root,width=1000, height =50, relief=SUNKEN)
Tops.pack(side=TOP)

s1 = Frame(root,width=600, height =300, relief=SUNKEN)
s1.pack(padx=10,pady=10)

#s2 = Frame(root,width=600, height =300,bg="powder blue", relief=SUNKEN)
#s2.pack(side=RIGHT)

lab1= Label(Tops, font=('arial',50,'bold'),text=" My Restaurant ", fg= "Green", bd=10,anchor='w')
lab1.grid(row=0,column=0)

ct=time.asctime(time.localtime(time.time()))
lab2= Label(Tops, font=('arial',20,'bold'),text=ct, fg= "Green", bd=10,anchor='w')
lab2.grid(row=1,column=0)

lab3= Label(s1, font=('arial',20,'bold'),text="Login-ID", fg= "Blue", bd=10,anchor='w')
lab3.grid(row=0,column=0)

text1=StringVar()
txtShow=Entry(s1,font=('arial',20,'bold'),textvariable=text1,bd=3,insertwidth=4,bg="powder blue", justify='left')
txtShow.grid(row=0,column=1)

lab4= Label(s1, font=('arial',20,'bold'),text="Password", fg= "Blue", bd=10,anchor='w')
lab4.grid(row=1,column=0)

text2=StringVar()
txtShow1=Entry(s1,font=('arial',20,'bold'),textvariable=text2,bd=3,insertwidth=4,bg="powder blue", justify='left', show='*')
txtShow1.grid(row=1,column=1)
def adduser():
        for widget in s1.winfo_children():
                widget.destroy()
        lab5= Label(s1, font=('arial',20,'bold'),text='Add New User', fg= "Blue", bd=10,anchor='w')
        lab5.grid(row=0,column=0)
        lab3= Label(s1, font=('arial',20,'bold'),text="User-ID", fg= "Blue", bd=10,anchor='w')
        lab3.grid(row=1,column=0)
        text1=StringVar()
        txtShow=Entry(s1,font=('arial',20,'bold'),textvariable=text1,bd=3,insertwidth=4,bg="powder blue", justify='left')
        txtShow.grid(row=0,column=1)

        lab4= Label(s1, font=('arial',20,'bold'),text="Password", fg= "Blue", bd=10,anchor='w')
        lab4.grid(row=1,column=0)

        text2=StringVar()
        txtShow1=Entry(s1,font=('arial',20,'bold'),textvariable=text2,bd=3,insertwidth=4,bg="powder blue", justify='left', show='*')
        txtShow1.grid(row=1,column=1)
     
        b2=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Submit", bg="powder blue", command=lambda:win1_bk.add(text1.get(),text2.get())).grid(row=3,column=1)
        
        b1=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Home", bg="powder blue", command=lambda:show_admin()).grid(row=4,column=1)

def deluser():
        for widget in s1.winfo_children():
                widget.destroy()
        lab5= Label(s1, font=('arial',20,'bold'),text='Delete User', fg= "Blue", bd=10,anchor='w')
        lab5.grid(row=0,column=0)
        lab3= Label(s1, font=('arial',20,'bold'),text="User-ID", fg= "Blue", bd=10,anchor='w')
        lab3.grid(row=1,column=0)
        text1=StringVar()
        txtShow=Entry(s1,font=('arial',20,'bold'),textvariable=text1,bd=3,insertwidth=4,bg="powder blue", justify='left')
        txtShow.grid(row=1,column=1)
        
        b2=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Delete", bg="powder blue", command=lambda:win1_bk.delete(text1.get())).grid(row=3,column=1)
        b1=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Home", bg="powder blue", command=lambda:show_admin()).grid(row=4,column=1)


def showuser():
        for widget in s1.winfo_children():
                widget.destroy()
        lab3= Label(s1, font=('arial',20,'bold'),text=" List of Users", fg= "Blue", bd=10,anchor='w')
        lab3.grid(row=0,column=1)
        lb=Listbox(s1,height=20,width=94)
        lb.grid(row=2,column=0,columnspan=6)
        #lb.delete(0,END)
        for row in win1_bk.viewall():
                lb.insert(END,row)
        
        b1=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Home", bg="powder blue", command=lambda:show_admin()).grid(row=8,column=1)

def show_admin():
        for widget in s1.winfo_children():
                widget.destroy()
        
        b1=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="create user", bg="powder blue", command=lambda:adduser()).grid(row=0,column=1)
        b2=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="delete user", bg="powder blue", command=lambda:deluser()).grid(row=1,column=1)
        b3=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="show users", bg="powder blue", command=lambda:showuser()).grid(row=2,column=1)
        b4=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Main Project", bg="powder blue", command=lambda:call_sys()).grid(row=3,column=1)

def Invent():
        for widget in s1.winfo_children():
                widget.destroy()
        import invent_restuarnt
        #invent_restuarnt.home()

def Bill():
        import bill_restuarnt;

        
def call_sys():
        for widget in s1.winfo_children():
                widget.destroy()
        #lab3= Label(s1, font=('arial',20,'bold'),text="Restaurant Billing" , fg= "Blue", bd=10,anchor='w')
        #lab3.grid(row=0,column=1)
        b1=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Inventory", bg="powder blue", command=lambda:Invent()).grid(row=0,column=1)
        b2=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Generate Bill", bg="powder blue", command=lambda:Bill()).grid(row=1,column=1)
        b3=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Exit Project", bg="powder blue", command=lambda:root.destroy()).grid(row=2,column=1)


def btnClick():
        
        if text1.get()=='admin' and text2.get()=='admin':
                show_admin()
        else:
                rows = win1_bk.search(text1.get(),text2.get())
                if not rows:
                       messagebox.showinfo(' wrong','try again')
                else:
                       if text1.get()== rows[0][1] and text2.get()== rows[0][2]:
                                #root.destroy()                       
                                call_sys()
         
        
btn1=Button(s1,padx=1,pady=10,bd=1,font=('arial',20),text="submit", bg="powder blue", command=lambda:btnClick()).grid(row=3,column=1)

root.mainloop()
