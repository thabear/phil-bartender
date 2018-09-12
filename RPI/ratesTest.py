###This GUI is primarily made for testing pour rates;
###not our final implementation


#Imports
import tkinter
from tkinter import messagebox
import pump

top = tkinter.Tk()

#Amount of time to run liqour (change to test)
liqTime = 30

#Amont of time to run soda (change to test)
sodaTime = 10

#API Calls; to be done by GUI button presses
def runLiq1():
    pump.liqour1Run(liqTime)
    messagebox.showinfo("Action Completed", "Liqour 1 run for {} secs".format(liqTime))

def runLiq2():
    pump.liqourRun(liqTime)
    messagebox.showinfo("Action Completed", "Liqour 2 run for {} secs".format(liqTime))

def runSoda():
    pump.sodaValveOpen()
    pump.sodaRun(sodaTime)
    pump.sodaValveClose()
    messagebox.showinfo("Ation Completed", "Soda opened, run for {} secs, and closed".format(sodaTime))


#GUI Buttons
btn_runLiqour1 = tkinter.Button(top, text = "Run Liqour 1", command = runLiq1)
btn_runLiqour2 = tkinter.Button(top, text = "Run Liqour 2", command = runLiq2)
btn_runSoda = tkinter.Button(top, text = "Run Soda", command = runSoda)



btn_runLiqour1.pack()
btn_runLiqour2.pack()
btn_runSoda.pack()
top.mainloop()
