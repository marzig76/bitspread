import sqlite3

class ratedata:

    conn = ""
    c = ""

    def __init__(self):
        self.conn = sqlite3.connect('../db/rates.db')
        self.c = self.conn.cursor()

    def rateinsert(self, rate, value):
        self.c.execute("INSERT INTO rate VALUES (?,?,datetime('now', 'localtime'))", (rate,value))
        self.conn.commit()

    def getlatestrate(self):
        query = "SELECT rate FROM rate WHERE dtg > datetime('now', '-2 minute', 'localtime') ORDER BY dtg DESC LIMIT 1"
        result = self.c.execute(query).fetchone()

        if result is not None:
            return result[0]
        else:
            return False

    def dataclose(self):
        self.conn.close()
