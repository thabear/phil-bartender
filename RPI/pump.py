from gpiozero import LED #LED IS OUR PUMP
from time import sleep #sleep is in seconds


liquorPump01 = LED(26)
liquorPump02 = LED(113)

sodaPump = LED(16)

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
