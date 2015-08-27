import time
import requests
from sqlite_class import ratedata

# setup db
datastore = ratedata()

# define api variables
base_url = "https://shapeshift.io"
pair = "btc_ltc"
apirate = "/rate/" + pair

while True:
    try:
        response = requests.get(base_url + apirate)

        if response.status_code == 200:
            content = response.json()

            for key, value in content.iteritems():
                if key == "rate":
                    datastore.rateinsert(pair,value)

        time.sleep(59)
    except:
        pass

datastore.dataclose
