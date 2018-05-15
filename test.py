import pymongo
import datetime


from pymongo import MongoClient
client = MongoClient()
db = client.mytest
print(db.dispositivi.find()[1])
disp1 = db.dispositivi.find({ "codDispositivo" : 1 })
print(disp1.count())
for elem in disp1:
	print(elem["login"])
disp2 = db.dispositivi.find({ "codDispositivo" : { "$gt" : 1 } })
print(disp2.count())

data = {
	"codDispositivo" : 4,
	"login" : datetime.datetime.utcnow(),
	"posizione" : {
		"lat" : 43.124522,
		"long" : 11.69423
	}
}

db.dispositivi.insert_one(data)
db.dispositivi.update(
	{"codDispositivo" : 4} ,
	{"$set" : {
		"marca" : "Il bambino che cresce sano"
		}
	})
