#wamp to create student record

from pymongo import *
con = None
try:
	con = MongoClient("mongodb://localhost:27017")
	db =  con["kit_28dec22"]
	coll = db["student"]
	rno = int(input("Enter rno "))
	count = coll.count_documents({"_id":rno})
	if count == 1:
		print("already exists ")
	else:
		info={"_id":rno}
		name = input("Enter name ")
		marks = input("Enter marks ")
		info["name"]=name
		info["marks"]=marks
		coll.insert_one(info)
		print(rno," created")
except Exception as e:
	print("issue ",e)
finally:
	if con is not None:
		con.close()