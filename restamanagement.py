import random
import time
import datetime
import tkinter.messagebox
from tkinter import *
root=Tk()
root.geometry("1350x750+0+0")
root.title("Cafe Management System")
root.configure(background='Cadet Blue')

Tops=Frame(root,bg='Cadet Blue', width=1350, height=100, bd=14,relief="raise")
Tops.pack(side=TOP)

f1=Frame(root, width=950,bg='Cadet Blue',height=650, bd=8,relief="raise")
f1.pack(side=LEFT)
f2=Frame(root, width=440, height=650, bd=8,relief="raise")
f2.pack(side=RIGHT)

ft2 = Frame(f2, width=440, height=650, bd=12,relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width=440, height=50, bd=16,relief="raise")
fb2.pack(side=BOTTOM)


f1a = Frame(f1, width=900, height=330,bg='Cadet Blue',bd=8,relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bg='Cadet Blue',bd=6,relief="raise")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=330, bd=16,relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=330, bd=16,relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=14,relief="raise")
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width=450, height=330, bd=14,relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='Cadet Blue')
f1.configure(background='Cadet Blue')
f2.configure(background='Cadet Blue')
##===============================================VARIABLES====
var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()
var9= IntVar()
var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()

DateofOrder=StringVar()
Receipt_Ref=StringVar()
CGST=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofDrinks=StringVar()
CostofSnacks=StringVar()
SGST=StringVar()

E_Tea=StringVar()
E_Milk=StringVar()
E_Coffe=StringVar()
E_Sprite=StringVar()
E_Pepsi=StringVar()
E_Limca=StringVar()
E_Laccy=StringVar()
E_Mazza=StringVar()

E_Idaly_Sambar=StringVar()
E_Dosa_Chutney=StringVar()
E_vadapav=StringVar()
E_Samosa=StringVar()
E_Veg_Burger=StringVar()
E_Patis=StringVar()
E_Maggy=StringVar()
E_Kande_Pohe=StringVar()

#===============================COSTOFITEM==================
def CostofItem():
    Item1=float(E_Tea.get())
    Item2=float(E_Milk.get())
    Item3=float(E_Coffe.get())
    Item4=float(E_Sprite.get())
    Item5=float(E_Pepsi.get())
    Item6=float(E_Limca.get())
    Item7=float(E_Laccy.get())
    Item8=float(E_Mazza.get())
    
    Item9=float(E_Idaly_Sambar.get())
    Item10=float(E_Dosa_Chutney.get())
    Item11=float(E_vadapav.get())
    Item12=float(E_Samosa.get())
    Item13=float(E_Veg_Burger.get())
    Item14=float(E_Patis.get())
    Item15=float(E_Maggy.get())
    Item16=float(E_Kande_Pohe.get())
   
   
    PriceofDrinks =(Item1 * 9.8) + (Item2 * 19.5) + (Item3 * 14.6) \
                    + (Item4 * 38.9) + (Item5 * 38.9) + (Item6 * 38.9) + (Item7 * 24.3) + (Item8 * 38.9)
    PriceofSnacks =(Item9 * 29.2) + (Item10 * 34) + (Item11 * 9.8) \
                    + (Item12 * 9.8) + (Item13 * 34) + (Item14 * 9.8) + (Item15 * 29.2) + (Item16 * 19.5)
    
    
    DrinksPrice ="Rs",str('%.2f'%(PriceofDrinks))
    SnacksPrice ="Rs",str('%.2f'%(PriceofSnacks))
    CostofDrinks.set(DrinksPrice)
    CostofSnacks.set(SnacksPrice)
    
    SubTotalofITEMS = "Rs",str('%.2f'%(PriceofDrinks + PriceofSnacks))
    SubTotal.set(SubTotalofITEMS)
    
    statetax="Rs",('%.2f'%((PriceofDrinks + PriceofSnacks)*0.015))
    SGST.set(statetax)
    centraltax="Rs",('%.2f'%((PriceofDrinks + PriceofSnacks)*0.015))
    CGST.set(centraltax)
    TT=(statetax + centraltax)
    TC="Rs",str('%.2f'%(PriceofDrinks + PriceofSnacks + TT))
    TotalCost.set(TC)
    
def iExit():
    iExit = tkinter.messagebox.askyesno("Exit Restaurant System","CONFIRM IF YOU WANT TO EXIT")
    if iExit > 0:
       root.destroy()
       return
    
def Reset():
    CGST.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofSnacks.set("")
    SGST.set("")
    txtReceipt.delete("1.0",END)
    
    E_Tea.set("0")
    E_Milk.set("0")
    E_Coffe.set("0")
    E_Sprite.set("0")
    E_Pepsi.set("0")
    E_Limca.set("0")
    E_Laccy.set("0")
    E_Mazza.set("0")
    E_Idaly_Sambar.set("0")
    E_Dosa_Chutney.set("0")
    E_vadapav.set("0")
    E_Samosa.set("0")
    E_Veg_Burger.set("0")
    E_Patis.set("0")
    E_Maggy.set("0")
    E_Kande_Pohe.set("0")
    
#===========================CHECKBUTTON===============================================
def chkbutton_value():
    if (var1.get() == 1):
        txtTea.configure(state=NORMAL)
    elif var1.get == 0:
         txtTea.configure(state=DISABLED)
         E_Tea.set("0")
    if (var2.get() == 1):
         txtMilk.configure(state= NORMAL)
    elif var2.get == 0:
         txtMilk.configure(state=DISABLED)
         E_Milk.set("0")
    if (var3.get() == 1):
        txtCoffe.configure(state=NORMAL)
    elif var3.get == 0:
            txtCoffe.configure(state=DISABLED)
            E_Coffe.set("0")
    if (var4.get() == 1):
        txtSprite.configure(state=NORMAL)
    elif var4.get == 0:
            txtSprite.configure(state=DISABLED)
            E_Sprite.set("0")
    if (var5.get() == 1):
        txtPepsi.configure(state=NORMAL)
    elif var5.get == 0:
            txtPepsi.configure(state=DISABLED)
            E_Pepsi.set("0")
    if (var6.get() == 1):
        txtLimca.configure(state=NORMAL)
    elif var6.get == 0:
            txtLimca.configure(state=DISABLED)
            E_Limca.set("0")
    if (var7.get() == 1):
        txtLaccy.configure(state=NORMAL)
    elif var7.get == 0:
            txtLaccy.configure(state=DISABLED)
            E_Laccy.set("0")
    if (var8.get() == 1):
        txtMazza.configure(state=NORMAL)
    elif var8.get == 0:
            txtMazza.configure(state=DISABLED)
            E_Mazza.set("0")
    if (var9.get() == 1):
        txtIdaly_Sambar.configure(state=NORMAL)
    elif var9.get == 0:
            txtIdaly_Sambar.configure(state=DISABLED)
            E_Idaly_Sambar.set("0")
    if (var10.get() == 1):
        txtDosa_Chutney.configure(state=NORMAL)
    elif var10.get == 0:
            txtDosa_Chutney.configure(state=DISABLED)
            E_Dosa_Chutney.set("0")
    if (var11.get() == 1):
        txtvadapav.configure(state=NORMAL)
    elif var11.get == 0:
            txtvadapav.configure(state=DISABLED)
            E_vadapav.set("0")
    if (var12.get() == 1):
        txtSamosa.configure(state=NORMAL)
    elif var12.get == 0:
            txtSamosa.configure(state=DISABLED)
            E_Samosa.set("0")
    if (var13.get() == 1):
        txtVeg_Burger.configure(state=NORMAL)
    elif var13.get == 0:
            txtVeg_Burger.configure(state=DISABLED)
            E_Veg_Burger.set("0")
    if (var14.get() == 1):
        txtPatis.configure(state=NORMAL)
    elif var14.get == 0:
            txtPatis.configure(state=DISABLED)
            E_Patis.set("0")
    if (var15.get() == 1):
        txtMaggy.configure(state=NORMAL)
    elif var15.get == 0:
            txtMaggy.configure(state=DISABLED)
            E_Maggy.set("0")
    if (var16.get() == 1):
        txtKande_Pohe.configure(state=NORMAL)
    elif var16.get == 0:
            txtKande_Pohe.configure(state=DISABLED)
            E_Kande_Pohe.set("0")
#======================================================================================
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")

    txtTea.configure(state=DISABLED)
    txtMilk.configure(state=DISABLED)
    txtCoffe.configure(state=DISABLED)
    txtSprite.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)
    txtLimca.configure(state=DISABLED)
    txtLaccy.configure(state=DISABLED)
    txtMazza.configure(state=DISABLED)
    txtIdaly_Sambar.configure(state=DISABLED)
    txtDosa_Chutney.configure(state=DISABLED)
    txtvadapav.configure(state=DISABLED)
    txtSamosa.configure(state=DISABLED)
    txtVeg_Burger.configure(state=DISABLED)
    txtPatis.configure(state=DISABLED)
    txtMaggy.configure(state=DISABLED)
    txtKande_Pohe.configure(state=DISABLED)

  
def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+randomRef)
    
    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+ Receipt_Ref.get() + '\t\t'+ DateofOrder.get()+"\n")
    txtReceipt.insert(END,'Items \t\t\t\t\t'+ "Cost of Items \n\n")
    txtReceipt.insert(END,'Tea: \t\t\t\t\t'+ E_Tea.get() + "\n")
    txtReceipt.insert(END,'Milk: \t\t\t\t\t'+ E_Milk.get() + "\n")
    txtReceipt.insert(END,'Coffe: \t\t\t\t\t'+ E_Coffe.get() + "\n")
    txtReceipt.insert(END,'Sprite: \t\t\t\t\t'+ E_Sprite.get() + "\n")
    txtReceipt.insert(END,'Pepsi: \t\t\t\t\t'+ E_Pepsi.get() + "\n")
    txtReceipt.insert(END,'Limca: \t\t\t\t\t'+ E_Limca.get() + "\n")
    txtReceipt.insert(END,'Laccy: \t\t\t\t\t'+ E_Laccy.get() + "\n")
    txtReceipt.insert(END,'Mazza: \t\t\t\t\t'+ E_Mazza.get() + "\n")
    txtReceipt.insert(END,'Idaly_Sambar: \t\t\t\t\t'+ E_Idaly_Sambar.get() + "\n")
    txtReceipt.insert(END,'Dosa_Chutney: \t\t\t\t\t'+ E_Dosa_Chutney.get() + "\n")
    txtReceipt.insert(END,'vadapav: \t\t\t\t\t'+ E_vadapav.get() + "\n")
    txtReceipt.insert(END,'Samosa: \t\t\t\t\t'+ E_Samosa.get() + "\n")
    txtReceipt.insert(END,'Veg_Burger: \t\t\t\t\t'+ E_Veg_Burger.get() + "\n")
    txtReceipt.insert(END,'Patis: \t\t\t\t\t'+ E_Patis.get() + "\n")
    txtReceipt.insert(END,'Maggy: \t\t\t\t\t'+ E_Maggy.get() + "\n")
    txtReceipt.insert(END,'Kande_Pohe: \t\t\t\t\t'+ E_Kande_Pohe.get() + "\n")
    txtReceipt.insert(END,'CostofDrinks:\t\t'+ CostofDrinks.get() + '\tCGST:\t\t' + CGST.get()+"\n")
    txtReceipt.insert(END,'CostofSnacks:\t\t'+ CostofSnacks.get() + '\tSubTotal:\t\t' + SubTotal.get()+"\n")
    txtReceipt.insert(END,'SGST:\t\t'+ SGST.get() + '\tTotalCost:\t\t' + TotalCost.get()+"\n")
    
##=================================================================================
##                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arial',70,'bold'),text="       Shaurya  Food  Court      \t ",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

DateofOrder.set(time.strftime("%d/%m/%y"))

##=================================================================================
##                  Drinks
#================================================================================

Tea = Checkbutton(f1aa, text="Tea.      \t\t", variable = var1, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 0, column=0, sticky=W)
Milk = Checkbutton(f1aa, text="Milk.        \t", variable = var2, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 1, column=0, sticky=W)
Coffe = Checkbutton(f1aa, text="Coffe.           \t", variable = var3, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 2, column=0, sticky=W)
Sprite= Checkbutton(f1aa, text="Sprite.           \t", variable = var4, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 3, column=0, sticky=W)
Pepsi= Checkbutton(f1aa, text="LPepsi.             \t", variable = var5, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 4, column=0, sticky=W)
Limca = Checkbutton(f1aa, text="Limca.             \t", variable = var6, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 5, column=0, sticky=W)
Laccy = Checkbutton(f1aa, text="Laccy.              \t", variable = var7, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 6, column=0, sticky=W)
Mazza = Checkbutton(f1aa, text="Mazza.            \t", variable = var8, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 7, column=0, sticky=W)
##=================================================================================
##                  Snacks
#================================================================================
Idaly_Sambar = Checkbutton(f1ab, text="Idaly_Sambar.  \t", variable = var9, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 0, column=0, sticky=W)
Dosa_Sambar = Checkbutton(f1ab, text="Dosa_chutney.   \t", variable = var10, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 1, column=0, sticky=W)
vadapav = Checkbutton(f1ab, text="vadapav.        \t", variable = var11, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 2, column=0, sticky=W)
Samosa = Checkbutton(f1ab, text="Samosa.            \t", variable = var12, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 3, column=0, sticky=W)
Veg_Burger = Checkbutton(f1ab, text="Veg_Burger.         \t\t", variable = var13, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 4, column=0, sticky=W)
Patis= Checkbutton(f1ab, text="Patis.                                  \t", variable = var14, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 5, column=0, sticky=W)
Maggy= Checkbutton(f1ab, text="Maggy.              \t", variable = var15, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 6, column=0, sticky=W)
Kande_Pohe= Checkbutton(f1ab, text="Kande_pohe.  \t", variable = var16, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold')).grid(row = 7, column=0, sticky=W)

##=================================================================================
##                  Enter WIDGET for drinks
#================================================================================
txtTea = Entry(f1aa,font=('arial',16,'bold'), bd=8,width=6, \
               justify='left',textvariable=E_Tea)
txtTea.grid(row=0, column=1)
txtMilk = Entry(f1aa,font=('arial',16,'bold'), bd=8,width=6,\
                justify='left',textvariable=E_Milk)
txtMilk.grid(row=1, column=1)
txtCoffe = Entry(f1aa,font=('arial',16,'bold'), bd=8,width=6,\
                 justify='left',textvariable=E_Coffe)
txtCoffe.grid(row=2, column=1)
txtSprite = Entry(f1aa,font=('arial',16,'bold'), bd=8,width=6,\
                  justify='left',textvariable=E_Sprite)
txtSprite.grid(row=3, column=1)
txtPepsi = Entry(f1aa,font=('arial',16,'bold'), bd=8,width=6,\
                 justify='left',textvariable=E_Pepsi)
txtPepsi.grid(row=4, column=1)
txtLimca = Entry(f1aa,font=('arial',16,'bold'), bd=8,width=6,\
                 justify='left',textvariable=E_Limca)
txtLimca.grid(row=5, column=1)
txtLaccy = Entry(f1aa,font=('arial',16,'bold'), bd=8,width=6,\
                 justify='left',textvariable=E_Laccy)
txtLaccy.grid(row=6, column=1)
txtMazza = Entry(f1aa,font=('arial',16,'bold'), bd=8,width=6,\
                 justify='left',textvariable=E_Mazza)
txtMazza.grid(row=7, column=1)
##=================================================================================
##                  Enter WIDGET for drinks
#==============================================================================
txtIdaly_Sambar = Entry(f1ab,font=('arial',16,'bold'), bd=8,width=6,\
                        justify='left',textvariable=E_Idaly_Sambar)
txtIdaly_Sambar.grid(row=0, column=2)
txtDosa_chutney = Entry(f1ab,font=('arial',16,'bold'), bd=8,width=6,\
                        justify='left',textvariable=E_Dosa_Chutney)
txtDosa_chutney.grid(row=1, column=2)
txtvadapav = Entry(f1ab,font=('arial',16,'bold'), bd=8,width=6,
                   justify='left',textvariable=E_vadapav)
txtvadapav.grid(row=2, column=2)
txtSamosa = Entry(f1ab,font=('arial',16,'bold'), bd=8,width=6,\
                  justify='left',textvariable=E_Samosa)
txtSamosa.grid(row=3, column=2)
txtVeg_Burger = Entry(f1ab,font=('arial',16,'bold'), bd=8,width=6,\
                      justify='left',textvariable=E_Veg_Burger)
txtVeg_Burger.grid(row=4, column=2)
txtPatis = Entry(f1ab,font=('arial',16,'bold'), bd=8,width=6,\
                 justify='left',textvariable=E_Patis)
txtPatis.grid(row=5, column=2)
txtMaggy = Entry(f1ab,font=('arial',16,'bold'), bd=8,width=6,\
                 justify='left',textvariable=E_Maggy)
txtMaggy.grid(row=6, column=2)
txtKande_Pohe = Entry(f1ab,font=('arial',16,'bold'), bd=8,width=6,\
                      justify='left',textvariable=E_Kande_Pohe)
txtKande_Pohe.grid(row=7, column=2)
##==========================INFORMATION======================================================:=
lblReceipt = Label(ft2,font=('arial',12,'bold'), text="Receipt", bd=2).grid(row=0,column=0, sticky=W)
txtReceipt = Text(ft2, width=59, height= 22, bg="white",bd=8, font=('arial',11,'bold'))
txtReceipt.grid(row=1,column=0)
##========================== Item INFORMATION==========================================
lblCostofDrinks=Label(f2aa,font=('arial',16,'bold'), text="CostofDrinks", bd=8)
lblCostofDrinks.grid(row=0,column=0,stick=W)
txtCostofDrinks=Entry(f2aa,font=('arial',16,'bold'), bd=8, justify='left',textvariable=CostofDrinks,bg='linen')
txtCostofDrinks.grid(row=0,column=1,stick=W)

lblCostofSnacks=Label(f2aa,font=('arial',16,'bold'), text="CostofSnacks", bd=8)
lblCostofSnacks.grid(row=1,column=0,stick=W)
txtCostofSnacks=Entry(f2aa,font=('arial',16,'bold'), bd=8, justify='left',textvariable=CostofSnacks,bg='linen')
txtCostofSnacks.grid(row=1,column=1,stick=W)

lblSGST=Label(f2aa,font=('arial',16,'bold'), text="SGST", bd=8)
lblSGST.grid(row=2,column=0,stick=W)
txtSGST=Entry(f2aa,font=('arial',16,'bold'), bd=8, justify='left',textvariable=SGST,bg='linen')
txtSGST.grid(row=2,column=1,stick=W)


##========================== Payment INFORMATION==========================================
lblCGST=Label(f2ab,font=('arial',16,'bold'), text="CGST", bd=8)
lblCGST.grid(row=0,column=0,stick=W)
txtCGST=Entry(f2ab,font=('arial',16,'bold'), bd=8,
                      insertwidth=2,justify='left',textvariable=CGST,bg='linen')
txtCGST.grid(row=0,column=1,stick=W)

lblSubTotal=Label(f2ab,font=('arial',16,'bold'), text="SubTotal ", bd=8)
lblSubTotal.grid(row=1,column=0,stick=W)
txtSubTotal=Entry(f2ab,font=('arial',16,'bold'), bd=8, justify='left',textvariable=SubTotal,bg='linen')
txtSubTotal.grid(row=1,column=1,stick=W)

lblTotalCost=Label(f2ab,font=('arial',16,'bold'), text="TotalCost", bd=8)
lblTotalCost.grid(row=2,column=0,stick=W)
txtTotalCost=Entry(f2ab,font=('arial',16,'bold'), bd=8, justify='left',textvariable=TotalCost,bg='linen')
txtTotalCost.grid(row=2,column=1,stick=W)

SGST.set("")
CGST.set("")
SubTotal.set("")
TotalCost.set("")
CostofDrinks.set("")
CostofSnacks.set("")
#===========================BUTTON==================================================
btnTotal=Button(fb2,padx=16,pady=1, bd=4, fg="black",font=('arial',16,'bold'), width=5,
                text="Total ", command=CostofItem).grid(row=0, column=0)
btnReceipt=Button(fb2,padx=16,pady=1, bd=4, fg="black",font=('arial',16,'bold'), width=5,
                text="Receipt ",command=Receipt).grid(row=0, column=1)
btnReset=Button(fb2,padx=16,pady=1, bd=4, fg="black",font=('arial',16,'bold'), width=5,
                text="Reset ",command=Reset).grid(row=0, column=2)
btnExit=Button(fb2,padx=16,pady=1, bd=4, fg="black",font=('arial',16,'bold'), width=5,
                text="Exit ",command=iExit).grid(row=0, column=3)



root.mainloop()
