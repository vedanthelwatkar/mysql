#wamp to read all student records

from pymongo import *
con = None
try:
	con = MongoClient("mongodb://localhost:27017")
	db = con["kit_28dec22"]
	coll = db["student"]

	data = coll.find()
	for d in data:
		print("rno = ",d["_id"],"name = ",d["name"],"marks = ",d["marks"])
except Exception as e:
	print("issue ",e)
finally:
	if con is not None:
		con.close()
