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

    def dataclose(self):
        self.conn.close()
