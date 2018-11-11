#API to run the pumps of PHIL from the RPI through the arduino that is hooked up

from gpiozero import LED #LED IS OUR PUMP
from time import sleep #sleep is in seconds


liquorPump01 = LED(26)
liquorPump02 = LED(13)

sodaPump = LED(16)
sodaValve = LED(6)

#Function : startUP : start all the pumps off because of the startup issues
def startUP():
  liquorPump01.off()
  liquorPump02.off()
  sodaPump.off()
  sodaValve.off()

#Function : liquor1Run : run the pump for the first liqor bottle
#Input : time : time in seconds to run the pump
#Output : void : no output 
def liquor1Run(time):
  liquorPump01.on()
  sleep(time)
  liquorPump01.off()
  
#Function : liquor2Run : run the pump for the second liqor bottle
#Input : time : time in seconds to run the pump
#Output : void : no output 
def liquor2Run(time):
  liquorPump02.on()
  sleep(time)
  liquorPump02.off()
  
#Function : Soda1Run : run the pump for the soda bottle
#Input : time : time in seconds to run the pump
#Output : void : no output 
def sodaRun(time):
  sodaPump.on()
  sleep(time)
  sodaPump.off()
  
#Function : sodaValveOpen : open the valve
#Input : none
#Output : none
def sodaValveOpen():
  sodaValve.on()

#Function : sodaValveClose : close the valve
#Input : none
#Output : none
def sodaValveClose():
  sodaValve.close()
