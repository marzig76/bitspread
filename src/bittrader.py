import json
from electrum_class import electrumapi


bitcoinwallet = electrumapi('btc')

testtx = bitcoinwallet.mktx('18jqWCXa3S53ewrop7Zgj4ccvNqBsJWmrt', "0.00553569")

jsontx = json.loads(testtx)

print jsontx['hex']

#testtx.broadcast(jsontx['hex'])
