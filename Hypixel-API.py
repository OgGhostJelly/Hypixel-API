#import modules
from requests import get as requests_get
from requests import exceptions as requests_exceptions
from concurrent.futures import ThreadPoolExecutor

from json import loads as json_loads

from nbt.nbt import NBTFile
from base64 import b64decode
from io import BytesIO

#get functions
def getAH():
    totalPages = requests_get('https://api.hypixel.net/skyblock/auctions').json()['totalPages']
    def getAHpages():
        #thread_function
        def thread_function(n):
            print('Requesting Page '+str(n+1)+'/'+str(totalPages))
            return requests_get('https://api.hypixel.net/skyblock/auctions?page='+str(n)).json()
        
        #ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=15) as executor:
            return executor.map(thread_function, range(3))#totalPages))
    
    def decode_NBT(raw):
        data = NBTFile(fileobj = BytesIO(b64decode(raw)))
        return data

    AH = []
    AHindexs = []
    AHcheapest = []

    for page in getAHpages():
        print('Processing Data...')
        if page['success']:
            AH.extend(page['auctions'])

    for auction in AH:
        auction_attributes = decode_NBT(auction['item_bytes'])[0][0]['tag']['ExtraAttributes']

        if str(auction_attributes['id']) == 'PET':
            auction_id = json_loads(str(auction_attributes['petInfo']))['type']
        else:
            auction_id = str(auction_attributes['id'])

        print(auction_id)
getAH()