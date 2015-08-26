from sqlite_class import ratedata


datastore = ratedata()

print datastore.getlatestrate()

datastore.dataclose()
