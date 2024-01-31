#wamp to delete student record

from pymongo import *
con = None
try:
	con = MongoClient("mongodb://localhost:27017")
	db = con["kit_28dec22"]
	coll = db["student"]
	
	rno = int(input("Enter rno "))
	count = coll.count_documents({"_id":rno})
	if count == 1:
		coll.delete_one({"_id":rno})
		print(rno," deleted")
	else:
		print(rno, " does not exists")
except Exception as e:
	print("issue ",e)
finally:
	if con is not None:
		con.close()
		