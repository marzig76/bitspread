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

    # get an receiving address that hasn't been used yet
    # this is not complete.. needs work
    def getrxaddress(self):
        command = self.coinbinary + " FILL THIS IN"
        output = execute(command, capture='True')
        return output

    # create and sign a bitcoin transaction
    # return the hex transaction to broadcast
    def mktx(self, recip, amount):
        if self.iscoinset():
            command = self.coinbinary + " payto -f " + self.fee + " " + recip + " " + amount
            output = execute(command, capture='True')
            return output
        else:
            return False

    # broadcast a transaction to the bitcoin network
    # use mktx to create a transaction to feed to this function
    def broadcast(self, tx):
        if self.iscoinset():
            command = self.coinbinary + " broadcast " + tx
            # is there output?
            return True
        else:
            return False

    # check whether or not a coin has been set
    def iscoinset(self):
        if self.coinbinary != "":
            return True
        else:
            return False
