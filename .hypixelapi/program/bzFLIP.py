from json import load as json_load
try:
    flip = json_load(open('.hypixelapi/data/BZ/flip.json'))
    raw = json_load(open('.hypixelapi/data/BZ/raw.json'))
except:
    print('Unable to get data, try running getBZ first then bzFLIP')
    exit()
try:
    price_limit = float(input('Price Limit >>> '))
except:
    price_limit = float('inf')
i = 0
for k,v in flip.items():
    if raw[k]['sell_summary'][0]['pricePerUnit'] >= price_limit:
        continue
    vn = str(len(flip)-i)+'. '+k
    print(vn,': ','Coin Per ( Hour: ',v['EstimatedProfitPerHour'],', Minute: ',v['EstimatedProfitPerMinute'],')',sep='')
    i += 1