import sqlite3
import collections

class ratedata:

    conn = ""
    c = ""

    # initialize the database connection
    def __init__(self):
        self.conn = sqlite3.connect('../db/rates.db')
        self.c = self.conn.cursor()

    # inserts a rate with the current timestamp
    def rateinsert(self, pair, rate):
        self.c.execute("INSERT INTO rate VALUES (?,?,datetime('now', 'localtime'))", (pair,rate))
        self.conn.commit()

    # inserts a trade with the current timestamp
    def tradeinsert(self, pair, rate, amount, src_addr, dst_addr):
        self.c.execute("INSERT INTO trade VALUES (?, ?, ?, ?, ?, datetime('now', 'localtime'))", (pair, rate, amount, src_addr, dst_addr))
        self.conn.commit()

    # returns the latest rate
    # if it's older than 2 minutes, return False
    # this ensures the rate that's returned is very recent
    def getlatestrate(self):
        query = "SELECT rate FROM rate WHERE dtg > datetime('now', '-2 minute', 'localtime') AND rate > 0 ORDER BY dtg DESC LIMIT 1"
        result = self.c.execute(query).fetchone()

        if result is not None:
            return result[0]
        else:
            return False

    # gets the latest trade details
    # returns an associative collection of the trade details
    def getlatesttrade(self):
        query = "SELECT pair, rate, amount, src_addr, dst_addr FROM trade ORDER BY dtg DESC LIMIT 1"
        result = self.c.execute(query).fetchone()

        if result is not None:
            trade = collections.defaultdict(dict)
            trade['pair'] = result[0]
            trade['rate'] = result[1]
            trade['amount'] = result[2]
            trade['src_addr'] = result[3]
            trade['dst_addr'] = result[4]

            return trade
        else:
            return False

    # closes the datastore connection
    def dataclose(self):
        self.conn.close()
