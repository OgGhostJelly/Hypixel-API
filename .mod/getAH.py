#mod
from requests import get as requests_get
from requests import exceptions as requests_exceptions
from json import dump as json_dump

#from base64 import b64decode
#from io import BytesIO
#from nbt.nbt import NBTFile
#def
def get_enchantedbook_name(item):
    for i,v in enumerate(item['item_lore']):
        if v == '§':
            item_lore = item['item_lore']
            item_lore = item_lore[:i] + item_lore[i+2:]
            item['item_lore'] = item_lore
        return item['item_lore'].split('\n')[0]
def request_data(url):
    try:
        return requests_get(url,timeout=(20,20)).json()
    except requests_exceptions.Timeout as e:
        print('TIMEOUT ERROR\n\nerr:',e)
        exit()
    except requests_exceptions.ConnectionError as e:
        print('CONNECTION ERROR\n\nerr:',e)
        exit()
    except requests_exceptions.RequestException as e:
        print('AN ERROR OCCURED\n\nerr:',e)
        exit()
#def nbt_data_Count(raw_data):
#    return int(NBTFile(fileobj = BytesIO(b64decode(raw_data)))['i'][0].get('Count').valuestr())

#request data
data = []
ahdata = request_data('https://api.hypixel.net/skyblock/auctions?page=0')
for i in range(ahdata['totalPages']-1):
    data.extend(ahdata['auctions'])
    progress = str(i+1)+'/'+str(ahdata['totalPages'])
    print('Requesting AH Data '+progress)
    ahdata = request_data('https://api.hypixel.net/skyblock/auctions?page='+str(i+1))
#create item dict / create item price
auction_item_name = {}
auction_item_cheap = {}
for i,v in enumerate(data):
    item_name = v['item_name']
    if item_name == 'Enchanted Book':
        item_name = get_enchantedbook_name(v)
    if not ( item_name in auction_item_name ):
        auction_item_name[item_name] = []
    if v['bin']:
        if not ( item_name in auction_item_cheap ):
            auction_item_cheap[item_name] = v
        elif auction_item_cheap[item_name]['starting_bid'] > v['starting_bid']:
            auction_item_cheap[item_name] = v

    auction_item_name[item_name].append(i)
    print('Processing AH Data '+str(i+1)+'/'+str(len(data)))
#write to files
print('Writing Data To JSON')
#json_dump(data, open(".mod/.data/AH/raw.json", "w"))
json_dump(auction_item_cheap, open(".mod/.data/AH/cheap.json", "w"))
#json_dump(auction_item_name, open(".mod/.data/AH/name.json", "w"))
print('Program Complete!')