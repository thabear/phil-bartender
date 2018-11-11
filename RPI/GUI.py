#Imports
import tkinter
from tkinter import messagebox
import pump

#Startup settings
#pump.startUP()

#Window Settings
mainWin = tkinter.Tk()
mainWin.geometry("500x250")
mainWin.resizable(False,False)

adminWin = tkinter.Tk()
adminWin.geometry("500x250")
adminWin.resizable(False,False)
adminWin.withdraw()

renameWin = tkinter.Tk()
renameWin.geometry("500x250")
renameWin.resizable(False,False)
renameWin.withdraw()

#Amount of time to run liqour (changeable)
liqTime = 26

#Amount of time to run soda (changeable)
sodaTime = 7

#Names for liqours and sodas (changeable via GUI)
liq1Name = "Whiskey"
liq2Name = "Rum"

soda1Name = "Coke"

#API Calls; to be done by GUI button presses
def runLiq1():
    pump.liquor1Run(liqTime)
    messagebox.showinfo("Action Completed", "{} run for {} secs".format(liq1Name,liqTime))

def runLiq2():
    pump.liquorRun(liqTime)
    messagebox.showinfo("Action Completed", "{} run for {} secs".format(liq2Name,liqTime))

def runSoda1():
    pump.sodaValveOpen()
    pump.sodaRun(sodaTime)
    pump.sodaValveClose()
    messagebox.showinfo("Action Completed", "{} opened, run for {} secs, and closed".format(soda1Name,sodaTime))

def runMix1():
    runLiq1()
    runSoda1()

def runMix2():
    runLiq2()
    runSoda1()

def admin():
    login(fld_Pword.get())
    
def login(pword):
    if pword == "password":
        mainWin.withdraw()
        adminWin.deiconify()
    else:
        messagebox.showinfo("ERROR", "Incorrect password. Please try again")
    
def renameDrinks():
    adminWin.withdraw()
    renameWin.deiconify()

def OLDrenameDrinks():
    print("What is the name of Liqour 1?")
    global liq1Name
    liq1Name = input(">>")
    print("What is the name of Liqour 2?")
    global liq2Name
    liq2Name = input(">>")
    print("What is the name of your soda?")
    global soda1Name
    soda1Name = input(">>")

def logs():
    messagebox.showinfo("LOG HIT","TODO: ADD LOG LOGIC")

def back():
    btn_Mix1.config(text="{} and {}".format(liq1Name, soda1Name))
    btn_Mix2.config(text="{} and {}".format(liq2Name, soda1Name))
    btn_Shot1.config(text="Shot of {}".format(liq1Name))
    btn_Shot2.config(text="Shot of {}".format(liq2Name))
    adminWin.withdraw()
    mainWin.deiconify()

def confirm():
    global liq1Name
    liq1Name = fld_liq1.get()
    global liq2Name
    liq2Name = fld_liq2.get()
    global soda1Name
    soda1Name = fld_soda1.get()
    renameWin.withdraw()
    adminWin.deiconify()
                        
###GUI Widget Creation
#Widgets for main user screen
btn_Mix1 = tkinter.Button(mainWin, text = "{} and {}".format(liq1Name, soda1Name),command = runMix1)
btn_Mix2 = tkinter.Button(mainWin, text = "{} and {}".format(liq2Name, soda1Name), command = runMix2)
btn_Shot1 = tkinter.Button(mainWin, text = "Shot of {}".format(liq1Name), command = runLiq1)
btn_Shot2 = tkinter.Button(mainWin, text = "Shot of {}".format(liq2Name), command = runLiq2)

btn_admin = tkinter.Button(mainWin, text = "Admin", command = admin)

fld_Pword = tkinter.Entry(mainWin, show="*")

#Widgets for admin screen
btn_renameDrinks = tkinter.Button(adminWin, text = "Edit Drinks", command = renameDrinks)
btn_back = tkinter.Button(adminWin, text = "<< Back", command = back)
btn_logs = tkinter.Button(adminWin, text = "View Logs", command = logs)

#Widgets for rename screen
btn_confirm = tkinter.Button(renameWin, text = "Confrim", command = confirm)

lbl_liq1 = tkinter.Label(renameWin, text = "Name of Liqour in pump 1:")
lbl_liq2 = tkinter.Label(renameWin, text = "Name of Liqour in pump 2:")
lbl_soda1 = tkinter.Label(renameWin, text = "Name of Soda:")

fld_liq1 = tkinter.Entry(renameWin)
fld_liq2 = tkinter.Entry(renameWin)
fld_soda1 = tkinter.Entry(renameWin)

###Widget Packing and Positioning
#Widgets in main user screen
btn_Mix1.place(x=75,y=45)
btn_Mix2.place(x=250,y=45)
btn_Shot1.place(x=75,y=90)
btn_Shot2.place(x=250,y=90)
btn_admin.place(x=300,y=180)

fld_Pword.place(x=350,y=185)

#Widgets in admin screen
btn_renameDrinks.place(x=225,y=50)
btn_logs.place(x=225,y=125)
btn_back.place(x=15,y=15)

#Widgets in rename screen
btn_confirm.place(x=250,y=185)

lbl_liq1.place(x=5,y=25)
lbl_liq2.place(x=5,y=100)
lbl_soda1.place(x=195,y=50)

fld_liq1.place(x=15,y=50)
fld_liq2.place(x=15,y=125)
fld_soda1.place(x=200,y=75)

###Calling mainWin so it actually shows up lol
mainWin.mainloop()
