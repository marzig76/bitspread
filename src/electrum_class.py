from executor import execute
import collections

class electrumapi:

    daemon = collections.defaultdict(dict)
    daemon["ltc"] = "electrum-ltc "
    daemon["btc"] = "electrum "

    def getnewaddress(self, coin):

        command = self.daemon[coin] + " getnewaddress"
        execute(command)

    def mktx(self, coin, recip, amount):

    def startdaemon(self, coin):
        command = self.daemon[coin] + " daemon start"
        execute(command)
