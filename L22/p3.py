import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyBsLXqOs48LVsanWT5qQDNSbNBTczvuNws",
  "authDomain": "employeepython3jan23-d2f84.firebaseapp.com",
  "databaseURL": "https://employeepython3jan23-d2f84-default-rtdb.firebaseio.com",
  "projectId": "employeepython3jan23-d2f84",
  "storageBucket": "employeepython3jan23-d2f84.appspot.com",
  "messagingSenderId": "675830438907",
  "appId": "1:675830438907:web:b28c1f809cacb518b1095e"
};

fb = pyrebase.initialize_app(firebaseConfig)
db = fb.database()

while True:
	op = int(input("1 create , 2 view , 3 remove , 4 exit " ))
	
	if op == 1:
		eid = int(input("Enter Employee ID "))
		data = db.child("employee").get()
		if (data.pyres is not None) and (str(eid) in data.val()):
			print(eid, " already exists")
		else:
			name = input("Enter yo name ")
			salary = float(input("Enter Salary "))
			info =  {"eid":eid,"name":name,"salary":salary}
			db.child("employee").child(eid).set(info)
			print(eid, " created")
	
	elif op == 2:
		data = db.child("employee").get()	
		if (data.pyres is not None):
			for d in data.each():
				print(d.val())
		else:
			print("data not found")
	
	elif op == 3:
		eid = int(input("Enter Employee ID "))
		data = db.child("employee").get()
		if (data.pyres is not None) and (str(eid) in data.val()):
			db.child("employee").child(eid).remove()
			print(eid," removed")
		else:
			print(eid, " not present")
	
	elif op == 4:
		break
	
	else:
		print("s i d u")		
			