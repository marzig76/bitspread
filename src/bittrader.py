import re
import json
import time
import datetime
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
def maketrade(pair, rate):
    # parse the pair to determine the starting coin and ending coin
    # the starting coin is the coin we're depositing to the exchange
    # the ending coin is the coin we're receiving from the exchange
    startingcoin = pair.split('_')[0]
    endingcoin = pair.split('_')[1]

    # initialize the crypto wrappers
    startingwallet = electrumapi(startingcoin)
    endingwallet = electrumapi(endingcoin)

    # get the balace of the starting coin
    startingcoinbalance = startingwallet.getbalance()

    # only initiate a trade if funds are available and all of these funds are confirmed
    if not startingcoinbalance:
        print datetime.datetime.now(), ": No balance to trade!"
        return False

    # define withdrawal and return addresses
    # the withdrawal address will be denominated in the ending coin
    # the return address will be denominated in the starting coin
    withdrawaladdress = endingwallet.getrxaddress()
    returnaddress = startingwallet.getrxaddress()

    # get a deposit address to send funds to
    exchange = exchangeapi()
    depositaddress = exchange.getdepositaddress(withdrawaladdress, pair, returnaddress)

    # determine the amount to send
    # take the balance and multiply it by the rate for that coin
    # subtract fee amount
    txamount = (startingcoinbalance * startingwallet.rate) - float(startingwallet.fee)

    # log trade info
    print "--------------------------------------"
    print datetime.datetime.now()
    print "Trade Pair:", pair
    print "Withdrawal Address:", withdrawaladdress
    print "Return Address:", returnaddress
    print "Deposit Address:", depositaddress
    print "Amount:", txamount
    print "--------------------------------------"

    # make and broadcast transaction
    tx = startingwallet.mktx(depositaddress, txamount)

    if tx:
        finalresult = startingwallet.broadcast(tx)

    # insert the trade into the database
    datastore = ratedata()
    datastore.tradeinsert(pair, rate, txamount, depositaddress, withdrawaladdress)

# enter service loop
while (True):

    # ALL THE LOGIC!!

    exit()
    time.sleep(59)
