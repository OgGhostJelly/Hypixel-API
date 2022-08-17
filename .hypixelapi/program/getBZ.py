#mod
from requests import get as requests_get
from requests import exceptions as requests_exceptions
from json import dump as json_dump
#request data
print('Requesting BZ Data 1/1')
try:
    raw = requests_get('https://api.hypixel.net/skyblock/bazaar',timeout=(20,20)).json()
    raw = raw['products']
except requests_exceptions.Timeout as e:
    print('TIMEOUT ERROR\n\nerr:',e)
    exit()
except requests_exceptions.ConnectionError as e:
    print('CONNECTION ERROR\n\nerr:',e)
    exit()
except requests_exceptions.RequestException as e:
    print('AN ERROR OCCURED\n\nerr:',e)
    exit()
#create flip dict
i = 1
flip = {}
for k,v in raw.items():
    try:
        flip[k] = round(v['buy_summary'][0]['pricePerUnit'] - v['sell_summary'][0]['pricePerUnit'],1)
    except:
        pass
    print('Processing BZ Data '+str(i)+'/'+str(len(raw)))
    i += 1
flip = dict(sorted(flip.items(), key=lambda item: item[1]))
#write to files
print('Writing Data To JSON')
json_dump(raw, open(".hypixelapi/data/BZ/raw.json", "w"))
json_dump(flip, open(".hypixelapi/data/BZ/flip.json", "w"))
print('Program Complete!')