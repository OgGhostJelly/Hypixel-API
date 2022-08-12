#mod
import json

#cheapest index
auction_item_cheap = json.load(open('data/AH/cheap.json'))
#bit items
bit_item = [
    { "item_name" : 'God Potion', "item_cost" : 1500 },
    { "item_name" : 'Kat Flower', "item_cost" : 500 },
    { "item_name" : 'Heat Core', "item_cost" : 3000 },
    { "item_name" : 'Hyper Catalyst Upgrade', "item_cost" : 300 },
    { "item_name" : 'Ultimate Carrot Candy Upgrade', "item_cost" : 8000 },
    { "item_name" : 'Colossal Experience Bottle Upgrade', "item_cost" : 1200 },
    { "item_name" : 'Jumbo Backpack Upgrade', "item_cost" : 4000 },
    { "item_name" : 'Minion Storage X-pender', "item_cost" : 1500 },
    { "item_name" : 'Hologram', "item_cost" : 2000 },
    { "item_name" : 'Builder\'s Wand', "item_cost" : 12000 },
    { "item_name" : 'Block Zapper', "item_cost" : 5000 },
    { "item_name" : 'Bits Talisman', "item_cost" : 15000 },
    { "item_name" : 'Autopet Rules 2-Pack', "item_cost" : 21000 },
    { "item_name" : 'Kismet Feather', "item_cost" : 1350 },
    { "item_name" : 'Inferno Fuel Block', "item_cost" : 500 },

    { "item_name" : 'Expertise I', "item_cost" : 4000 },
    { "item_name" : 'Compact I', "item_cost" : 4000 },
    { "item_name" : 'Cultivating I', "item_cost" : 4000 },
    { "item_name" : 'Champion I', "item_cost" : 4000 },
    { "item_name" : 'Hecatomb I', "item_cost" : 6000 },

    { "item_name" : 'Speed Enrichment', "item_cost" : 5000 },
    { "item_name" : 'Intelligence Enrichment', "item_cost" : 5000 },
    { "item_name" : 'Critical Damage Enrichment', "item_cost" : 5000 },
    { "item_name" : 'Critical Chance Enrichment', "item_cost" : 5000 },
    { "item_name" : 'Strength Enrichment', "item_cost" : 5000 },
    { "item_name" : 'Defense Enrichment', "item_cost" : 5000 },
    { "item_name" : 'Health Enrichment', "item_cost" : 5000 },
    { "item_name" : 'Magic Find Enrichment', "item_cost" : 5000 },
    { "item_name" : 'Ferocity Enrichment', "item_cost" : 5000 },
    { "item_name" : 'Sea Creature Chance Enrichment', "item_cost" : 5000 },
    { "item_name" : 'Attack Speed Enrichment', "item_cost" : 5000 },
    { "item_name" : 'Accessory Enrichment Swapper', "item_cost" : 200 },
]

#calculate bit prices
auction_item_bit = {}
for i,v in enumerate(bit_item):
    if v['item_name'] in auction_item_cheap:
        auction_item_bit[v['item_name']] = auction_item_cheap[v['item_name']]['starting_bid']/v['item_cost']
auction_item_bit = dict(sorted(auction_item_bit.items(), key=lambda item: item[1]))
auction_item_bit = dict(reversed(auction_item_bit.items()))

for v in auction_item_bit:
    print(v,'-',auction_item_bit[v],'-',auction_item_cheap[v]['starting_bid'])