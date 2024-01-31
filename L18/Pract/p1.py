#wapp to create a record


from pymongo import *
con = None
try:
	con = MongoClient("mongodb://localhost:27017")
	db = con["kc_28dec22"]
	coll  = db["emp"]
	i = int(input("Enter emp id "))
	count = coll.count_documents({"_id":i})
	if count == 1:
		 print("already exists")
	else:
		info={"_id":i}
		res= input("do you want to enter name y/n ")
		if res == "y":
			name = input("Enter emp name ")
			info["name"] = name
		res= input("do you want to enter salary y/n ")
		if res == "y":
			salary = input("Enter emp salary ")
			info["salary"]=salary
		coll.insert_one(info)
		print(i," created")
except Exception as e:
	prin("issue ", e)
finally:
	if con is not None:
		con.close()