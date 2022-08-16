from json import load as json_load
try:
    auction_item_mode = json_load(open('.mod/.data/AH/mode.json'))
except:
    print('Unable to get data, try running getAH.py first then calcAHmode.py')
    exit()
try:
    inpt = input('Item to Calculate >>> ')
    print(inpt+': ',auction_item_mode[inpt])
except:
    print('Invalid Item Check Capitalization')
    exit()