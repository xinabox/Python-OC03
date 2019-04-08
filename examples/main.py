from OC03 import OC03
from microbit import *

OC03 = OC03()

# start OC03
OC03.init()

# sleep time
DELAY = 500

# infinite loop
while True:

    # close relay
    OC03.writePin(True)		
    sleep(DELAY)
    
    # open relay
    OC03.writePin(False)
    sleep(DELAY)
