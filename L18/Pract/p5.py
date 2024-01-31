#wamp to update records

from pymongo import *
con = None
try:
	con = MongoClient("mongodb://localhost:27017")
	db = con["kit_28dec22"]
	coll = db["student"]

	rno = int(input("Enter rno "))
	count =  coll.count_documents({"_id":rno})
	if count == 1:
		info = {}
		name = input("Enter name ")
		marks = int(input("Enter marks "))
		info["name"]=name
		info["marks"]=marks
		ndata = {"$set":info}
		coll.update_one({"_id":rno},ndata)
		print(rno," updated")
	else:
		print(rno , "does not exists")
except Exception as e:
	print("issue ",e)
finally:
	if con is not None:
		con.close()
