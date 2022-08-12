#mod
import json

#cheapest index
try:
    auction_item_cheap = json.load(open('.data/AH/cheap.json'))
except:
    print('Unable to get data, try running getAH.py first')
    exit()
#bit items
bit_item = {
    'God Potion' : 1500,
    'Kat Flower' : 500,
    'Heat Core' : 3000,
    'Hyper Catalyst Upgrade' : 300,
    'Ultimate Carrot Candy Upgrade' : 8000,
    'Colossal Experience Bottle Upgrade' : 1200,
    'Jumbo Backpack Upgrade' : 4000,
    'Minion Storage X-pender' : 1500,
    'Hologram' : 2000,
    'Builder\'s Wand' : 12000,
    'Block Zapper' : 5000,
    'Bits Talisman' : 15000,
    'Autopet Rules 2-Pack' : 21000,
    'Kismet Feather' : 1350,
    'Inferno Fuel Block' : 500,

    'Expertise I' : 4000,
    'Compact I' : 4000,
    'Cultivating I' : 4000,
    'Champion I' : 4000,
    'Hecatomb I' : 6000,

    'Speed Enrichment' : 5000,
    'Intelligence Enrichment' : 5000,
    'Critical Damage Enrichment' : 5000,
    'Critical Chance Enrichment' : 5000,
    'Strength Enrichment' : 5000,
    'Defense Enrichment' : 5000,
    'Health Enrichment' : 5000,
    'Magic Find Enrichment' : 5000,
    'Ferocity Enrichment' : 5000,
    'Sea Creature Chance Enrichment' : 5000,
    'Attack Speed Enrichment' : 5000,
    'Accessory Enrichment Swapper' : 200,
}

#calculate bit prices
auction_item_bit = {}
for i,item_name in enumerate(bit_item):
    if item_name in auction_item_cheap:
        item_cost = bit_item[item_name]
        auction_item_bit[item_name] = auction_item_cheap[item_name]['starting_bid']/item_cost
auction_item_bit = dict(sorted(auction_item_bit.items(), key=lambda item: item[1]))
#print data
for i,v in enumerate(auction_item_bit):
    vn = str(len(auction_item_bit)-i)+'. '+v
    cpb = str(auction_item_bit[v])+'/bit '
    vbc_vcc = '('+ str(bit_item[v])+', '+str(auction_item_cheap[v]['starting_bid'])+')'

    print(vn,': ',cpb,vbc_vcc,sep='')