#wamp to view all records

from pymongo import *
con = None
try:
	con =MongoClient("mongodb://localhost:27017")
	db = con["kc_28dec22"]
	coll = db["emp"]

	data = coll.find()
	for d in data:
		print(d)
except Exception as e:
	print("issue ",e)
finally:
	if con is not None:
		con.close()
