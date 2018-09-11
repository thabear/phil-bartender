import pump
from time import sleep

# run for 30 seconds to pour a shot?
pump.liquor1Run(30)
pump.liquor2Run(30)

# run soda pump for 5 seconds to pour just shy of a glass?
pump.sodaValveOpen()
pump.sodaRun(5)
pump.sodaValveClose()

sleep(5)

# test results
