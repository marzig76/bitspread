import json
import time
from restful_lib import Connection
from sqlite_class import ratedata

# setup db
datastore = ratedata()

# connect to shapeshift
base_url = "https://shapeshift.io"
apiconn = Connection(base_url)

rate = "btc_ltc"
ssrate = "/rate/" + rate

while 1:
    # checking exchange rate
    getrate = apiconn.request(ssrate)

    # extract the body of the response
    for item in getrate:
        if item == "body":
            response = json.loads(getrate[item])

    # extract the rate
    for key, value in response.iteritems():
        if key == "rate":
            datastore.rateinsert(rate,value)

    time.sleep(60)

datastore.dataclose
