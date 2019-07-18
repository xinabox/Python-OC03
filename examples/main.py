from xOC03 import xOC03
from xCore import xCore

OC03 = xOC03()

# start OC03
OC03.init()

# sleep time
DELAY = 500

# infinite loop
while True:

    # close relay
    OC03.writePin(True)		
    xCore.sleep(DELAY)
    
    # open relay
    OC03.writePin(False)
    xCore.sleep(DELAY)
