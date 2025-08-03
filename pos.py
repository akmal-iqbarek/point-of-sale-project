from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Point of Sale(Bill/mgmt)")
root.resizable(False,False)

def Reset():
    entry_kiribath.delete(0,END)
    entry_polrotti.delete(0,END)
    entry_parippuvade.delete(0,END)
    entry_aappa.delete(0,END)
    entry_milktea.delete(0,END)
    entry_plaintea.delete(0,END)
    entry_kiritoffee.delete(0,END)

def Total():
    try:a1=int(kiribath.get())
    except:a1=0

    try:a2=int(polrotti.get())
    except:a2=0

    try:a3=int(parippuvade.get())
    except:a3=0

    try:a4=int(aappa.get())
    except:a4=0

    try:a5=int(milktea.get())
    except:a5=0

    try:a6=int(plaintea.get())
    except:a6=0

    try:a7=int(kiritoffee.get())
    except:a7=0

    #define cost of each item seperately
    c1=60*a1
    c2=50*a2
    c3=50*a3
    c4=40*a4
    c5=60*a5
    c6=30*a6
    c7=10*a7

    lbl_total=Label(f2,font=('aria',20,'bold'),text='Total',width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)




    
Label(text="Point of Sale(Akmal/Store)", bg="black", fg="white", font=("calibri", 33), width="300", height="2").pack()

#MENU CARD
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabrio",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Kiribath--Rs.60/piece",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Pol Rotti-Rs.50/piece",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="ParipuVade--Rs.50/piece",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Aappa--Rs.40/piece",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Milk Tea--Rs.60/cup",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Plain Tea--Rs.30/cup",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Kiri toffee--Rs.10/piece",fg="black",bg="lightgreen").place(x=10,y=260)

#BILL
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=("calibri",20),bg='lightyellow')
Bill.place(x=120,y=10)

#ENTRY WORK
f1=Frame(root,bd=5,height=37,width=300,relief=RAISED)
f1.pack()


kiribath=StringVar()
polrotti=StringVar()
parippuvade=StringVar()
aappa=StringVar()
milktea=StringVar() 
plaintea=StringVar()
kiritoffee=StringVar()
Total_bill=StringVar()

#Label
lbl_kiribath=Label(f1,font=("aria",20,'bold'),text="Kiribath",width=12,fg="blue4")
lbl_polrotti=Label(f1,font=("aria",20,'bold'),text="Pol Rotti",width=12,fg="blue4")
lbl_parippuvade=Label(f1,font=("aria",20,'bold'),text="Parippu Vade",width=12,fg="blue4")
lbl_aappa=Label(f1,font=("aria",20,'bold'),text="Aappa",width=12,fg="blue4")
lbl_milktea=Label(f1,font=("aria",20,'bold'),text="Milk Tea",width=12,fg="blue4")
lbl_plaintea=Label(f1,font=("aria",20,'bold'),text="Plain Tea",width=12,fg="blue4")
lbl_kiritoffee=Label(f1,font=("aria",20,'bold'),text="Kiri toffee",width=12,fg="blue4")

lbl_kiribath.grid(row=1,column=0)
lbl_polrotti.grid(row=2,column=0)
lbl_parippuvade.grid(row=3,column=0)
lbl_aappa.grid(row=4,column=0)
lbl_milktea.grid(row=5,column=0)
lbl_plaintea.grid(row=6,column=0)
lbl_kiritoffee.grid(row=7,column=0)

#Entry
entry_kiribath = Entry(f1, font=("aria", 20, "bold"), textvariable=kiribath, bd=6, width=8, bg="lightpink")
entry_polrotti = Entry(f1, font=("aria", 20, "bold"), textvariable=polrotti, bd=6, width=8, bg="lightpink")
entry_parippuvade = Entry(f1, font=("aria", 20, "bold"), textvariable=parippuvade, bd=6, width=8, bg="lightpink")
entry_aappa = Entry(f1, font=("aria", 20, "bold"), textvariable=aappa, bd=6, width=8, bg="lightpink")
entry_milktea = Entry(f1, font=("aria", 20, "bold"), textvariable=milktea, bd=6, width=8, bg="lightpink")
entry_plaintea = Entry(f1, font=("aria", 20, "bold"), textvariable=plaintea, bd=6, width=8, bg="lightpink")
entry_kiritoffee = Entry(f1, font=("aria", 20, "bold"), textvariable=kiritoffee, bd=6, width=8, bg="lightpink")

entry_kiribath.grid(row=1, column=1)
entry_polrotti.grid(row=2, column=1)
entry_parippuvade.grid(row=3, column=1)
entry_aappa.grid(row=4, column=1)
entry_milktea.grid(row=5, column=1)
entry_plaintea.grid(row=6, column=1)
entry_kiritoffee.grid(row=7, column=1)


#buttons


btn_reset=Button(f1, bd=5, fg="black", bg="lightblue", font=("arial", 16, 'bold'), width=10, text="Reset", command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1, bd=5, fg="black", bg="lightblue", font=("arial", 16, 'bold'), width=10, text="Total", command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()
