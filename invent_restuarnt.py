from tkinter import*
from tkinter import messagebox
import random
import time
import datetime
#import win1_bk


root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")

Tops=Frame(root, width=100,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=1800,height=700,relief=SUNKEN)
f1.pack(padx=10,pady=10)


localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arial',50,'bold'),text=" INVENTORY OF RESTAURANT ",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

        
Idly=StringVar()
Dosa=StringVar()
Kesari=StringVar()
Pulav=StringVar()
Drinks=StringVar()

           
def qExit():
    root.destroy()


    
#====================================Restaraunt Info 1===========================================================
    
def showinvent():
        for widget in f1.winfo_children():
                widget.destroy()
        lab3= Label(f1, font=('arial',20,'bold'),text=" List of Stocks", fg= "Blue", bd=10,anchor='w')
        lab3.grid(row=0,column=1)
        lb=Listbox(f1,height=20,width=94)
        lb.grid(row=2,column=0,columnspan=6)
        #lb.delete(0,END)
        import win1_bk
        rows=win1_bk.viewstock()
        lb.insert(END,'IDLY   : ',rows[0][1])
        lb.insert(END,'DOSA   : ',rows[0][2])
        lb.insert(END,'KESARI : ',rows[0][3])
        lb.insert(END,'DRINKS : ',rows[0][4])
        lb.insert(END,'PULAV  : ',rows[0][5])
        b1=Button(f1,padx=20,pady=10,bd=2,font=('arial',20),text="Home", bg="powder blue", command=lambda:home()).grid(row=8,column=1)

def upd():
        messagebox.showinfo(Idly.get(),Dosa.get())
        #win1_bk.update(1,Idly.get(),Dosa.get(),Kesari.get(),Drinks.get(),Pulav.get())

def invent():
        for widget in f1.winfo_children():
            widget.destroy()
        lblIdly= Label(f1, font=('arial', 16, 'bold'),text="Idly",bd=16,anchor="w")
        lblIdly.grid(row=0, column=0)
        Idly=StringVar()
        #e4 = Entry(window,textvariable=category,width=50)
        txtIdly=Entry(f1, font=('arial',16,'bold'),textvariable=Idly)#,bd=1,insertwidth=4,bg="powder blue",justify='left')
        txtIdly.grid(row=0,column=1)


        lblDosa= Label(f1, font=('arial', 16, 'bold'),text="Dosa",bd=16,anchor="w")
        lblDosa.grid(row=1, column=0)
        Dosa=StringVar()
        txtDosa=Entry(f1, font=('arial',16,'bold'),textvariable=Dosa)#,bd=1,insertwidth=4,bg="powder blue",justify='left')
        txtDosa.grid(row=1,column=1)


        lblKesari= Label(f1, font=('arial', 16, 'bold'),text="Kesari bath",bd=16,anchor="w")
        lblKesari.grid(row=2, column=0)
        Kesari=StringVar()
        txtKesari=Entry(f1, font=('arial',16,'bold'),textvariable=Kesari)#,bd=1,insertwidth=4,bg="powder blue",justify='left')
        txtKesari.grid(row=2,column=1)

        lblPulav= Label(f1, font=('arial', 16, 'bold'),text="Pulav",bd=16,anchor="w")
        lblPulav.grid(row=3, column=0)
        Pulav=StringVar()
        txtPulav=Entry(f1, font=('arial',16,'bold'),textvariable=Pulav)#,bd=1,insertwidth=4,bg="powder blue",justify='left')
        txtPulav.grid(row=3,column=1)

        lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
        lblDrinks.grid(row=4, column=0)
        Drinks=StringVar()
        txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks)#,bd=1,insertwidth=4,bg="powder blue",justify='left')
        txtDrinks.grid(row=4,column=1)
              
        import win1_bk
        b1=Button(f1,padx=20,pady=10,bd=2,font=('arial',20),text="Update", bg="powder blue", command=lambda:win1_bk.update(1,Idly.get(),Dosa.get(),Kesari.get(),Drinks.get(),Pulav.get())).grid(row=5,column=1)
        b2=Button(f1,padx=20,pady=10,bd=2,font=('arial',20),text="Home", bg="powder blue", command=lambda:home()).grid(row=8,column=1)

def home():
    for widget in f1.winfo_children():
        widget.destroy()
    b1=Button(f1,padx=20,pady=10,bd=2,font=('arial',20),text=" Update Inventory", bg="powder blue", command=lambda:invent()).grid(row=0,column=1)
    b2=Button(f1,padx=20,pady=10,bd=2,font=('arial',20),text="Show Inventory", bg="powder blue", command=lambda:showinvent()).grid(row=1,column=1)
    b3=Button(f1,padx=20,pady=10,bd=2,font=('arial',20),text="Exit Project ", bg="powder blue", command=lambda:root.destroy()).grid(row=2,column=1)

home()
root.mainloop()


