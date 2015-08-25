import json
from executor import execute

class electrumapi:

    # the binary to be called
    coinbinary = ""
    fee = ".0001"

    def __init__(self, coin):
        self.setcoin(coin)

    # set the coin.. right now it only supports bitcoin and litecoin
    def setcoin(self, coin):
        if coin == 'btc':
            self.coinbinary = "electrum "
        elif coin == 'ltc':
            self.coinbinary = "electrum-ltc "
        else:
            return False

        return True

    # get a receiving address that hasn't been used yet
    def getrxaddress(self):
        # first get a list of available addresses
        getaddresses = self.listaddresses()
        addresslist = json.loads(getaddresses)

        # for each address, check to see if it's ever been used before
        for address in addresslist:
            gethistory = self.getaddresshistory(address)
            historylist = json.loads(gethistory)

            # once we find an address that hasn't been used (history is empty), return that address
            if historylist == []:
                return address

        return False

    # create and sign a transaction
    # return the hex transaction to broadcast
    def mktx(self, recip, amount):
        if self.iscoinset():
            command = self.coinbinary + " payto -f " + self.fee + " " + recip + " " + amount
            output = execute(command, capture='True')
            return output
        else:
            return False

    # broadcast a transaction to the network
    # use mktx to create a transaction to feed to this function
    def broadcast(self, tx):
        if self.iscoinset():
            command = self.coinbinary + " broadcast " + tx
            output = execute(command, capture='True')
            return True
        else:
            return False

    # check whether or not a coin has been set
    def iscoinset(self):
        if self.coinbinary != "":
            return True
        else:
            return False

    # standard electrum command - lists addresses
    def listaddresses(self):
        if self.iscoinset():
            command = self.coinbinary + " listaddresses"
            output = execute(command, capture='True')
            return output
        else:
            return False

    # standard electrum command - gets the history of an address
    def getaddresshistory(self, address):
        if self.iscoinset():
            command = self.coinbinary + " getaddresshistory " + address
            output = execute(command, capture='True')
            return output
        else:
            return False
