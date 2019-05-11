from tkinter import*
from tkinter import messagebox
import random
import time
import win1_bk


root=Tk()
root.geometry("1600x8000")
root.title("My Restaurant")

Tops = Frame(root,width=100, relief=SUNKEN)
Tops.pack(side=TOP)

s1 = Frame(root,width=1800, height =700, relief=SUNKEN)
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
rand = StringVar()

Idly=StringVar()
Dosa=StringVar()
Kesari=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Pulav=StringVar()

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

#====================================Restaraunt Info 1===========================================================
def Invent():
        for widget in s1.winfo_children():
                widget.destroy()
                 
        Idly=StringVar()
        Dosa=StringVar()
        Kesari=StringVar()
        Pulav=StringVar()
        Drinks=StringVar()
        home()

def qExit():
    root.destroy()


    
def showinvent():
        for widget in s1.winfo_children():
                widget.destroy()
        lab3= Label(s1, font=('arial',20,'bold'),text=" List of Stocks", fg= "Blue", bd=10,anchor='w')
        lab3.grid(row=0,column=1)
        lb=Listbox(s1,height=20,width=94)
        lb.grid(row=2,column=0,columnspan=6)
        #lb.delete(0,END)
        import win1_bk
        rows=win1_bk.viewstock()
        lb.insert(END,'IDLY   : ',rows[0][1])
        lb.insert(END,'DOSA   : ',rows[0][2])
        lb.insert(END,'KESARI : ',rows[0][3])
        lb.insert(END,'DRINKS : ',rows[0][4])
        lb.insert(END,'PULAV  : ',rows[0][5])
        b1=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Home", bg="powder blue", command=lambda:home()).grid(row=8,column=1)

def upd():
        messagebox.showinfo(Idly.get(),Dosa.get())
        #win1_bk.update(1,Idly.get(),Dosa.get(),Kesari.get(),Drinks.get(),Pulav.get())

def invent():
        for widget in s1.winfo_children():
            widget.destroy()
        lblhd= Label(s1, font=('arial', 16, 'bold'),text="Update the current Quantity",bd=16,anchor="w")
        lblIdly= Label(s1, font=('arial', 16, 'bold'),text="Idly",bd=16,anchor="w")
        lblIdly.grid(row=1, column=0)
        Idly=StringVar()
        #e4 = Entry(window,textvariable=category,width=50)
        txtIdly=Entry(s1, font=('arial',16,'bold'),textvariable=Idly)#,bd=1,insertwidth=4,bg="powder blue",justify='left')
        txtIdly.grid(row=1,column=1)


        lblDosa= Label(s1, font=('arial', 16, 'bold'),text="Dosa",bd=16,anchor="w")
        lblDosa.grid(row=2, column=0)
        Dosa=StringVar()
        txtDosa=Entry(s1, font=('arial',16,'bold'),textvariable=Dosa)#,bd=1,insertwidth=4,bg="powder blue",justify='left')
        txtDosa.grid(row=2,column=1)


        lblKesari= Label(s1, font=('arial', 16, 'bold'),text="Kesari bath",bd=16,anchor="w")
        lblKesari.grid(row=3, column=0)
        Kesari=StringVar()
        txtKesari=Entry(s1, font=('arial',16,'bold'),textvariable=Kesari)#,bd=1,insertwidth=4,bg="powder blue",justify='left')
        txtKesari.grid(row=3,column=1)

        lblPulav= Label(s1, font=('arial', 16, 'bold'),text="Pulav",bd=16,anchor="w")
        lblPulav.grid(row=4, column=0)
        Pulav=StringVar()
        txtPulav=Entry(s1, font=('arial',16,'bold'),textvariable=Pulav)#,bd=1,insertwidth=4,bg="powder blue",justify='left')
        txtPulav.grid(row=4,column=1)

        lblDrinks= Label(s1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
        lblDrinks.grid(row=5, column=0)
        Drinks=StringVar()
        txtDrinks=Entry(s1, font=('arial',16,'bold'),textvariable=Drinks)#,bd=1,insertwidth=4,bg="powder blue",justify='left')
        txtDrinks.grid(row=5,column=1)
            
        b1=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Update", bg="powder blue", command=lambda:win1_bk.update(1,Idly.get(),Dosa.get(),Kesari.get(),Drinks.get(),Pulav.get())).grid(row=8,column=1)
        b2=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Home", bg="powder blue", command=lambda:home()).grid(row=10,column=1)

def home():
    for widget in s1.winfo_children():
        widget.destroy()
    b1=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text=" Update Inventory", bg="powder blue", command=lambda:invent()).grid(row=0,column=1)
    b2=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Show Inventory", bg="powder blue", command=lambda:showinvent()).grid(row=1,column=1)
    b3=Button(s1,padx=20,pady=10,bd=2,font=('arial',20),text="Home ", bg="powder blue", command=lambda:call_sys()).grid(row=2,column=1)

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)

    rand.set(randomRef)

    if (Idly.get()==""):
        CoIdly=0
    else:
        CoIdly=float(Idly.get())

  
    if (Dosa.get()==""):
        CoDosa=0
    else:
        CoDosa=float(Dosa.get())

    if (Kesari.get()==""):
        CoKesari=0
    else:
        CoKesari=float(Kesari.get())

    if (Pulav.get()==""):
        CoPulav=0
    else:
        CoPulav=float(Pulav.get())
        
     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())
                   
    CostofIdly =CoIdly * 25
    CostofDrinks=CoD * 20
    CostofDosa = CoDosa* 35
    CostofKesari = CoKesari * 25
    CostPulav = CoPulav* 35
    
    CostofMeal= "Rs", str('%.2f' % (CostofIdly+CostofDrinks+CostofDosa+CostofKesari+CostPulav))

    PayTax=((CostofIdly+CostofDrinks+CostofDosa+CostofKesari+CostPulav) * 0.2)

    TotalCost=(CostofIdly+CostofDrinks+CostofDosa+CostofKesari+CostPulav)
 
    Ser_Charge= ((CostofIdly+CostofDrinks+CostofDosa+CostofKesari+CostPulav)/99)

    Service = "Rs", str ('%.2f' % Ser_Charge)

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    win1_bk.updateB(1,Idly.get(),Dosa.get(),Kesari.get(),Drinks.get(),Pulav.get())
    
def Reset():
    rand.set("") 
    Idly.set("")
    Dosa.set("")
    Kesari.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Pulav.set("")
    


def Bill():
        for widget in s1.winfo_children():
                widget.destroy()
        
                                       
        lblReference= Label(s1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
        lblReference.grid(row=0, column=0)
        
        txtReference=Entry(s1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtReference.grid(row=0,column=1)

        lblIdly= Label(s1, font=('arial', 16, 'bold'),text="Idly",bd=16,anchor="w")
        lblIdly.grid(row=1, column=0)
        txtIdly=Entry(s1, font=('arial',16,'bold'),textvariable=Idly,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtIdly.grid(row=1,column=1)


        lblDosa= Label(s1, font=('arial', 16, 'bold'),text="Dosa",bd=16,anchor="w")
        lblDosa.grid(row=2, column=0)
        txtDosa=Entry(s1, font=('arial',16,'bold'),textvariable=Dosa,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtDosa.grid(row=2,column=1)


        lblKesari= Label(s1, font=('arial', 16, 'bold'),text="Kesari bath",bd=16,anchor="w")
        lblKesari.grid(row=3, column=0)
        txtKesari=Entry(s1, font=('arial',16,'bold'),textvariable=Kesari,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtKesari.grid(row=3,column=1)

        lblPulav= Label(s1, font=('arial', 16, 'bold'),text="Pulav",bd=16,anchor="w")
        lblPulav.grid(row=4, column=0)
        txtPulav=Entry(s1, font=('arial',16,'bold'),textvariable=Pulav,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtPulav.grid(row=4,column=1)

        
        lblDrinks= Label(s1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
        lblDrinks.grid(row=0, column=2)
        txtDrinks=Entry(s1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtDrinks.grid(row=0,column=3)

        lblCost= Label(s1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
        lblCost.grid(row=1, column=2)
        txtCost=Entry(s1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtCost.grid(row=1,column=3)


        lblService= Label(s1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
        lblService.grid(row=2, column=2)
        txtService=Entry(s1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtService.grid(row=2,column=3)


        lblStateTax= Label(s1, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
        lblStateTax.grid(row=3, column=2)
        txtStateTax=Entry(s1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtStateTax.grid(row=3,column=3)

        lblSubTotal= Label(s1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
        lblSubTotal.grid(row=4, column=2)
        txtSubTotal=Entry(s1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtSubTotal.grid(row=4,column=3)

        lblTotalCost= Label(s1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
        lblTotalCost.grid(row=5, column=2)
        txtTotalCost=Entry(s1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtTotalCost.grid(row=5,column=3)
        Reset()

        #==========================================Buttons==========================================================================================
        btnTotal=Button(s1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=lambda:Ref()).grid(row=7,column=1)

        btnReset=Button(s1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=lambda:Reset()).grid(row=7,column=2)

        btnExit=Button(s1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Home",bg="powder blue",command=lambda:call_sys()).grid(row=7,column=3)

                
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
