###This GUI is for our demo video, and only has one button


#Imports
import tkinter
from tkinter import messagebox
#import pump

#Window Settings
top = tkinter.Tk()
top.geometry("500x250")

#Amount of time to run liqour
liqTime = 30

#Amont of time to run soda - 7 = one shot?
sodaTime = 7

#API Calls; to be done by GUI button presses
def runLiq1():
    pump.liquor1Run(liqTime)

def runSoda():
    pump.sodaValveOpen()
    pump.sodaRun(sodaTime)
    pump.sodaValveClose()

def pourItUp():
    runLiq1()
    runSoda()


#GUI Buttons
btn_pour = tkinter.Button(top, text = "Whiskey Coke", command = pourItUp)

btn_pour.pack(pady=75)
top.mainloop()
