#Imports
import tkinter
from tkinter import messagebox
import sqlite3
#import pump

#Open db connection and set db cursor
conn = sqlite3.connect('phil.db')
curs = conn.cursor()

#Startup settings (if needed)
#pump.startUP()

#Window Settings
mainWin = tkinter.Tk()
mainWin.geometry("600x300")
mainWin.resizable(False,False)

drinkWin = tkinter.Tk()
drinkWin.geometry("600x300")
drinkWin.resizable(False,False)
drinkWin.withdraw()

#Amount of time to run liquor
liqTime = 25
#Amount of time to run soda (changeable)
sodaTime = 5

#Dink Configuration
class Drink:
    Name = "Not Set"
    #Num of shots (for liq) or num cups (soda)
    liq1 = 0
    liq2 = 0
    soda = 0
    cost = 0

    def setName(self, name):
        self.Name = name
    def getName(self):
        print(self.Name)
        
    def getPump1(self):
        return self.liq1
    def getPump2(self):
        return self.liq2
    def getSoda(self):
        return self.soda
    def getCost(self):
        return self.cost

    def setInfo(self, liquor1, liquor2, sodaPump, cost):
        self.liq1 = liquor1
        self.liq2 = liquor2
        self.soda = sodaPump
        self.cost = cost

    def addSale(self, drink):
        curs.execute('INSERT INTO drinkSales(drinkName) VALUES(?)', (drink,))

drink1 = Drink()
drink2 = Drink()
drink3 = Drink()
drink4 = Drink()

#Initialize some default drinks:
def createDrinks():
    drink1.setName("Double Whiskey Coke")
    drink1.setInfo(2,0,1,5.25)

    drink2.setName("Whiskey Coke")
    drink2.setInfo(1,0,1,3.00)

    drink3.setName("Shot of Whiskey")
    drink3.setInfo(1,0,0,3.00)

    drink4.setName("5 shots of Whiskey lol")
    drink4.setInfo(5,0,0,12.00)

#Comment out the below line to make it start as if
#PHIL is right out of the box:
createDrinks()

#Currently/Last Selected Drink
currDrink = "NONE"
#Current/Last Drink that was edited
currEdit = "NONE"

#API Calls; to be done by GUI button presses
def runLiq1():
    #pump.liquor1Run(liqTime)
    #messagebox.showinfo("Action Completed", "Drink Poured.")
    print("ran Liq 1")

def runLiq2():
    #pump.liquor2Run(liqTime)
    #messagebox.showinfo("Action Completed", "Drink Poured.")
    print("ran Liq 2")

def runSoda1():
    #pump.sodaValveOpen()
    #pump.sodaRun(sodaTime)
    #pump.sodaValveClose()
    #messagebox.showinfo("Action Completed", "Drink Poured.")
    print("ran Soda")
    
#Button Commands:
def cleanFields():
    fld_drinkName.delete(0,"end")
    fld_pump1.delete(0,"end")
    fld_pump2.delete(0,"end")
    fld_pump3.delete(0,"end")
    fld_cost.delete(0,"end")
    fld_startDate.delete(0,"end")
    fld_endDate.delete(0,"end")
    
def edit1():
    cleanFields()
    global currEdit
    currEdit = 1
    mainWin.withdraw()
    drinkWin.deiconify()
    lbl_currDrink.config(text="[{}]".format(drink1.Name))
    lbl_currPump1.config(text="[{}]".format(drink1.getPump1()))
    lbl_currPump2.config(text="[{}]".format(drink1.getPump2()))
    lbl_currPump3.config(text="[{}]".format(drink1.getSoda()))
    lbl_currCost.config(text="[{}]".format(drink1.getCost()))

def edit2():
    cleanFields()
    global currEdit
    currEdit = 2
    mainWin.withdraw()
    drinkWin.deiconify()
    lbl_currDrink.config(text="[{}]".format(drink2.Name))
    lbl_currPump1.config(text="[{}]".format(drink2.getPump1()))
    lbl_currPump2.config(text="[{}]".format(drink2.getPump2()))
    lbl_currPump3.config(text="[{}]".format(drink2.getSoda()))
    lbl_currCost.config(text="[{}]".format(drink2.getCost()))

def edit3():
    cleanFields()
    global currEdit
    currEdit = 3
    mainWin.withdraw()
    drinkWin.deiconify()
    lbl_currDrink.config(text="[{}]".format(drink3.Name))
    lbl_currPump1.config(text="[{}]".format(drink3.getPump1()))
    lbl_currPump2.config(text="[{}]".format(drink3.getPump2()))
    lbl_currPump3.config(text="[{}]".format(drink3.getSoda()))
    lbl_currCost.config(text="[{}]".format(drink3.getCost()))

def edit4():
    cleanFields()
    global currEdit
    currEdit = 4
    mainWin.withdraw()
    drinkWin.deiconify()
    lbl_currDrink.config(text="[{}]".format(drink4.Name))
    lbl_currPump1.config(text="[{}]".format(drink4.getPump1()))
    lbl_currPump2.config(text="[{}]".format(drink4.getPump2()))
    lbl_currPump3.config(text="[{}]".format(drink4.getSoda()))
    lbl_currCost.config(text="[{}]".format(drink4.getCost()))

def admin():
    login(fld_pword.get())

def login(pword):
    if pword == "password":
        toggleState(True)
    else:
        messagebox.showinfo("Login Error","Incorrect Password. Please Try Again.")

def toggleState(admin):
    if admin:
        btn_Edit1.config(state="normal")
        btn_Edit2.config(state="normal")
        btn_Edit3.config(state="normal")
        btn_Edit4.config(state="normal")
        btn_logs.config(state="normal")
        btn_logoff.config(state="normal")
        fld_startDate.config(state="normal")
        fld_endDate.config(state="normal")
    else:
        btn_Edit1.config(state="disabled")
        btn_Edit2.config(state="disabled")
        btn_Edit3.config(state="disabled")
        btn_Edit4.config(state="disabled")
        btn_logs.config(state="disabled")
        btn_logoff.config(state="disabled")
        fld_startDate.config(state="disabled")
        fld_endDate.config(state="disabled")

def logs():
    messagebox.showinfo("LOGS HIT","Add Log logic here pls")

def confirm():
    if currEdit == 1:
        drink1.setName(fld_drinkName.get())
        drink1.setInfo(int(fld_pump1.get()),int(fld_pump2.get()),int(fld_pump3.get()),float(fld_cost.get()))
        btn_Drink1.config(text=drink1.Name)
    elif currEdit == 2:
        drink2.setName(fld_drinkName.get())
        drink2.setInfo(int(fld_pump1.get()),int(fld_pump2.get()),int(fld_pump3.get()),float(fld_cost.get()))
        btn_Drink2.config(text=drink2.Name)
    elif currEdit == 3:
        drink3.setName(fld_drinkName.get())
        drink3.setInfo(int(fld_pump1.get()),int(fld_pump2.get()),int(fld_pump3.get()),float(fld_cost.get()))
        btn_Drink3.config(text=drink3.Name)
    elif currEdit == 4:
        drink4.setName(fld_drinkName.get())
        drink4.setInfo(int(fld_pump1.get()),int(fld_pump2.get()),int(fld_pump3.get()),float(fld_cost.get()))
        btn_Drink4.config(text=drink4.Name)

    drinkWin.withdraw()
    mainWin.deiconify()

def cancel():
    drinkWin.withdraw()
    mainWin.deiconify()

def logoff():
    toggleState(False)
    fld_pword.delete(0,"end")

def pour1():
    global currDrink
    currDrink = drink1
    if drink1.liq1 > 0:
        for i in range(1,drink1.liq1+1):
            runLiq1()
    if drink1.liq2 > 0:
        for i in range(1,drink1.liq2+1):
            runLiq2()
    if drink1.soda > 0:
        for i in range(1,drink1.soda+1):
            runSoda1()

    drink1.addSale(currDrink.Name)

def pour2():
    global currDrink
    currDrink = drink2
    if drink2.liq1 > 0:
        for i in range(1,drink2.liq1+1):
            runLiq1()
    if drink2.liq2 > 0:
        for i in range(1,drink2.liq2+1):
            runLiq2()
    if drink2.soda > 0:
        for i in range(1,drink2.soda+1):
            runSoda1()
    drink2.addSale(currDrink.Name)

def pour3():
    global currDrink
    currDrink = drink3
    if drink3.liq1 > 0:
        for i in range(1,drink3.liq1+1):
            runLiq1()
    if drink3.liq2 > 0:
        for i in range(1,drink3.liq2+1):
            runLiq2()
    if drink3.soda > 0:
        for i in range(1,drink3.soda+1):
            runSoda1()
    

def pour4():
    global currDrink
    currDrink = drink4
    if drink4.liq1 > 0:
        for i in range(1,drink4.liq1+1):
            runLiq1()
    if drink4.liq2 > 0:
        for i in range(1,drink4.liq2+1):
            runLiq2()
    if drink4.soda > 0:
        for i in range(1,drink4.soda+1):
            runSoda1()

###GUI Widget Creation:
#Widgets for mainWin
btn_Drink1 = tkinter.Button(mainWin,text=drink1.Name,command=pour1,height=4,width=20)
btn_Drink2 = tkinter.Button(mainWin,text=drink2.Name,command=pour2,height=4,width=20)
btn_Drink3 = tkinter.Button(mainWin,text=drink3.Name,command=pour3,height=4,width=20)
btn_Drink4 = tkinter.Button(mainWin,text=drink4.Name,command=pour4,height=4,width=20)

btn_Edit1 = tkinter.Button(mainWin,text="edit",command=lambda: edit1(),height=1,width=3,state="disabled")
btn_Edit2 = tkinter.Button(mainWin,text="edit",command=lambda: edit2(),height=1,width=3,state="disabled")
btn_Edit3 = tkinter.Button(mainWin,text="edit",command=lambda: edit3(),height=1,width=3,state="disabled")
btn_Edit4 = tkinter.Button(mainWin,text="edit",command=lambda: edit4(),height=1,width=3,state="disabled")

btn_admin = tkinter.Button(mainWin,text="Admin",command=admin)
btn_logs = tkinter.Button(mainWin,text="Logs",command=logs,state="disabled")
btn_logoff = tkinter.Button(mainWin,text="Log Off",command=logoff,state="disabled")

fld_pword = tkinter.Entry(mainWin, show="*")
fld_startDate = tkinter.Entry(mainWin,width=13,state="disabled")
fld_endDate = tkinter.Entry(mainWin,width=13,state="disabled")

lbl_date = tkinter.Label(mainWin,text="to")

#Widgets for drink config screen
btn_confirm = tkinter.Button(drinkWin,text="Confirm",command=confirm)
btn_cancel = tkinter.Button(drinkWin,text="Cancel",command=cancel)

lbl_drinkName = tkinter.Label(drinkWin,text="Name of Drink")
lbl_pump1 = tkinter.Label(drinkWin,text="Liquour pump 1? (# of Shots)")
lbl_pump2 = tkinter.Label(drinkWin,text="Liquour pump 2? (# of Shots)")
lbl_pump3 = tkinter.Label(drinkWin,text="Soda pump? (# of Cups)")
lbl_cost = tkinter.Label(drinkWin,text="Cost? (written in form 00.00)")

lbl_currDrink = tkinter.Label(drinkWin,text="")
lbl_currPump1 = tkinter.Label(drinkWin,text="")
lbl_currPump2 = tkinter.Label(drinkWin,text="")
lbl_currPump3 = tkinter.Label(drinkWin,text="")
lbl_currCost = tkinter.Label(drinkWin,text="")

fld_drinkName = tkinter.Entry(drinkWin)
fld_pump1 = tkinter.Entry(drinkWin)
fld_pump2 = tkinter.Entry(drinkWin)
fld_pump3 = tkinter.Entry(drinkWin)
fld_cost = tkinter.Entry(drinkWin)

###Widget Packing and Positioning:
#Widgets in mainWin
btn_Drink1.place(x=30,y=30)
btn_Drink2.place(x=300,y=30)
btn_Drink3.place(x=30,y=150)
btn_Drink4.place(x=300,y=150)

btn_Edit1.place(x=180,y=75)
btn_Edit2.place(x=450,y=75)
btn_Edit3.place(x=180,y=195)
btn_Edit4.place(x=450,y=195)

btn_admin.place(x=400,y=250)
btn_logs.place(x=85,y=250)
btn_logoff.place(x=30,y=250)

fld_pword.place(x=450,y=252)
fld_startDate.place(x=125,y=253)
fld_endDate.place(x=205,y=253)

lbl_date.place(x=190,y=250)

#Widgets in drinkWin
btn_confirm.place(x=300,y=260)
btn_cancel.place(x=225,y=260)

lbl_drinkName.place(x=160,y=25)
lbl_pump1.place(x=160,y=75)
lbl_pump2.place(x=160,y=125)
lbl_pump3.place(x=160,y=175)
lbl_cost.place(x=160, y=225)

lbl_currDrink.place(x=15,y=25)
lbl_currPump1.place(x=15,y=75)
lbl_currPump2.place(x=15,y=125)
lbl_currPump3.place(x=15,y=175)
lbl_currCost.place(x=15,y=225)

fld_drinkName.place(x=260,y=25)
fld_pump1.place(x=335,y=80)
fld_pump2.place(x=335,y=130)
fld_pump3.place(x=310,y=180)
fld_cost.place(x=335,y=225)

###Calling mainWin so it actually shows up lol:
mainWin.mainloop()

#close db connection
conn.close()

