import json
import requests

class exchangeapi:

    # set up default values
    base_url = "https://shapeshift.io"
    pair = "btc_ltc"
    apirate = "/rate/"
    apishift = "/shift/"

    def __init__(self, url = ""):
        if url != "":
            self.base_url = url

    def getrate(self, pair = ""):
        if pair != "":
            self.pair = pair

        response = requests.get(self.base_url + self.apirate + self.pair)

        if response.status_code == 200:
            content = response.json()

            for key, value in content.iteritems():
                if key == "rate":
                    return value

    def getdepositaddress(self, withdrawaladdress, pair):
        post_data = {"withdrawal":withdrawaladdress, "pair":pair}

        shift = requests.post(self.base_url + self.apishift, post_data)

        if shift.status_code == 200:
            response = json.loads(shift.content)

            for key, value in response.iteritems():
                if key == "deposit":
                    return value
                elif key == "error":
                    return False
        else:
            return False
