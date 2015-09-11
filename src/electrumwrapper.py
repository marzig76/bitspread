import json
from executor import execute

class electrumapi:

    coinbinary = ""     # the binary to be called
    fee = ".0001"       # the fee to use
    rate = 0            # what percentage of the total balance to be traded

    def __init__(self, coin):
        self.setcoin(coin)

    # set the coin.. right now it only supports bitcoin and litecoin
    def setcoin(self, coin):
        if coin == 'btc':
            self.coinbinary = "electrum "
            self.rate = .75
        elif coin == 'ltc':
            self.coinbinary = "electrum-ltc "
            self.rate = 1
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

            # once we find an address that hasn't been used (history is empty), return that address
            # sometimes the history is completely empty, sometimes it's an empty json set - check both
            if not gethistory:
                return address
            else:
                historylist = json.loads(gethistory)

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

    def daemon(self, control):
        if self.iscoinset() and (control == 'start' or control == 'stop'):
            command = self.coinbinary + " daemon " + control
            output = execute(command, capture='True')
            return True
        else:
            return False

    def getbalance(self):
        if self.iscoinset():
            command = self.coinbinary + " getbalance "
            output = execute(command, capture='True')
            balance = json.loads(output)

            for key, value in balance.iteritems():
                if key == 'confirmed':
                    returnbalance = value
                elif key == 'unconfirmed':
                    return False

            return returnbalance
        else:
            return False
