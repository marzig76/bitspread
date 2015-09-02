from sqlite_class import ratedata


datastore = ratedata()



# insert rate
#datastore.rateinsert("test", 99.99)

# insert trade
datastore.tradeinsert("ltc_btc", 0.014285714, 1.5, "L3dasda", "1zasdfe")

# get latest rate
#print "rate", datastore.getlatestrate()

# get latest trade
result = datastore.getlatesttrade()
print result['pair'], result['rate'], result['amount'], result['src_addr'], result['dst_addr']

#print pair, rate, amount, src_addr, dst_addr

datastore.dataclose()
