#mod
from json import load as json_load
#get data
err = False
try:
    AH_raw = json_load(open('.hypixelapi/data/AH/raw.json'))
    AH_name = json_load(open('.hypixelapi/data/AH/name.json'))
except:
    print('Unable to get data, try running getAH first then pet')
    err = True
try:
    BZ_raw = json_load(open('.hypixelapi/data/BZ/raw.json'))
except:
    print('Unable to get data, try running getBZ first then pet')
    err = True
if err:
    exit()
del err
#pet data
