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

    # get a rate for any pair of currencies
    def getrate(self, pair = ""):
        if pair != "":
            self.pair = pair

        response = requests.get(self.base_url + self.apirate + self.pair)

        if response.status_code == 200:
            content = response.json()

            for key, value in content.iteritems():
                if key == "rate":
                    return value

        return False

    # in order to make a trade, you need to send a withdrawal address and a coin pair.
    # pass those two parameters and get back a deposit address.
    # anything deposited to that address will be converted (according to the specified currency pair)
    # and sent to your withdrawal address
    # in case something goes wrong, your inital deposit will be sent back to the return address
    def getdepositaddress(self, withdrawaladdress, pair, returnaddress):
        post_data = {"withdrawal":withdrawaladdress, "pair":pair, "returnAddress":returnaddress}

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
