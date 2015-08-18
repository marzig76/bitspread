import time
import requests
from sqlite_class import ratedata

# setup db
datastore = ratedata()

# define api variables
base_url = "https://shapeshift.io"
rate = "btc_ltc"
apirate = "/rate/" + rate

while True:
    response = requests.get(base_url + apirate)

    if response.status_code == 200:
        content = response.json()

        for key, value in content.iteritems():
            if key == "rate":
                datastore.rateinsert(rate,value)

    time.sleep(59)

datastore.dataclose
