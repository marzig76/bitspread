import json
import time
import requests
from sqlite_class import ratedata
from electrumwrapper import electrumapi
from shapeshiftwrapper import exchangeapi

# initialize datastore
datastore = ratedata()

# initialize the crypto wrappers
bitcoinwallet = electrumapi('btc')
litecoinwallet = electrumapi('ltc')

# define trade api variables
exchange = exchangeapi()

# enter service loop

while (True):
    # Get last rate
    #latestrate = datastore.getlatestrate()

    # Get latest trade
    #latesttrade = datastore.getlatesttrade()

    # work on this logic..    
    newaddress = litecoinwallet.getrxaddress()
    depositaddress = exchange.getdepositaddress(newaddress, "btc_ltc")

    print "final response: ", depositaddress

    time.sleep(59)
