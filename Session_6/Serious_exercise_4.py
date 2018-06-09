import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client= MongoClient(mongo_uri)
db = client.get_default_database()
customers = db["customers"]

wom = int(db.customers.count({"ref":"wom"}))
print(wom)

ads = int(db.customers.count({"ref":"ads"}))
print(ads)

events = int(db.customers.count({"ref":"events"}))
print(events)

labels = ["wom", "ads","events"]
color = ["blue", "green", "red"]
value =[wom,ads,events]
explode = (0,0,0.1)

pyplot.pie(value, labels = labels,colors = color, explode = explode, shadow = True)

pyplot.axis("equal")

pyplot.show()
