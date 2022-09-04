#import modules
from requests import get as requests_get
from requests import exceptions as requests_exceptions
from concurrent.futures import ThreadPoolExecutor

#get functions
def getAH():
    def getAHpages():
        #thread_function
        def thread_function(n):
            print('Getting Page '+str(n))
            return requests_get('https://api.hypixel.net/skyblock/auctions?page='+str(n)).json()
        
        #ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=10) as executor:
            return executor.map(thread_function, range(requests_get('https://api.hypixel.net/skyblock/auctions').json()['totalPages']+1))

    AH = []
    AHindexs = []
    AHcheapest = []

    for page in getAHpages():
        if page['success']:
            AH.extend(page['auctions'])

    for auction in AH:
        pass
getAH()