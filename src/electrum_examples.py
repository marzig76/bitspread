import json
from electrum_class import electrumapi

# create wallet instance
bitcoinwallet = electrumapi('btc')

# get a rx address
address = bitcoinwallet.getrxaddress()

# mktx
testtx = bitcoinwallet.mktx(address, "0.00543569")
jsontx = json.loads(testtx)
print testtx, jsontx['hex']

# broadcast
#result = bitcoinwallet.broadcast(jsontx['hex'])

print result
