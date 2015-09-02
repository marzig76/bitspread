import re
import json
import time
import requests
from sqlite_class import ratedata
from electrumwrapper import electrumapi
from shapeshiftwrapper import exchangeapi

# initialize datastore
datastore = ratedata()

# acceptable percentage from previous trade
pct = 1.04

# put this in a util class?
# simple rate swap..
# if 1 btc is worth 80 ltc,
# then 1 ltc is worth 1/80 btc
def rateswap(rate):
    return 1 / rate

# all the steps to make a trade
# should split this out more..
def maketrade(pair):
    # initialize the crypto wrappers
    bitcoinwallet = electrumapi('btc')
    litecoinwallet = electrumapi('ltc')

    # define trade api variables
    exchange = exchangeapi()

    # we only want to trade if we have confirmed balances
    # get the balance of the starting coin
    startingcoin = pair.split('_')[0]

    litecoinaddress = litecoinwallet.getrxaddress()
    bitcoinaddress = bitcoinwallet.getrxaddress()

    if startingcoin == 'btc':
        balance = bitcoinwallet.getbalance()
        withdrawaladdress = litecoinaddress
        returnaddress = bitcoinaddress
        rate = 0.75 # convert this percentage of BTC to LTC
    elif startingcoin == 'ltc':
        balance = litecoinwallet.getbalance()
        withdrawaladdress = litecoinaddress
        returnaddress = bitcoinaddress
        rate = 1    # always convert entire LTC balance bat to BTC
    else:
        return False

    if balance:
        print "true: ", balance
    else:
        return False

    depositaddress = exchange.getdepositaddress(withdrawaladdress, pair, returnaddress)

    #make and broadcast transaction



# enter service loop
while (True):

    # ALL THE LOGIC!!

    exit()
    time.sleep(59)
