class Employee:
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary

	def show(self):
		print("name=",self.name)
		print("salary=",self.salary)

	def computeTax(self):
		ta=0.0
		if self.salary>50000:
			ta=self.salary*0.20
		else:
			ta=self.salary*0.10
		print("tax amount=",ta)

data={}
while True
	op==int(input(1 add,2 show,3 remove and 4 exit))
	if op==1:
		id=int(input("enter your id"))
		if data.get(id) = None:
			name=input("enter your name"))
			salary=int(input("enter your salary"))
			e=Employee(name,salary)
			data[id]=e
			print(id , "is added")
		else:
			print(id , "already exists")
	

	elif op==2:
		for d in data:
			print("id=", d)
			data[d].show()
			data[d].computeTax()
			print("*" * 50)
	
	elif op==3:
		id=int(input("enter the id you want to remove")
		if data.get(id) is not None:
			data.pop(id)
			print(id, " is removed") 
		else:
			print(id, " dosen't exists")

	elif op==4:
		break
	
	else:
		print("s i d u ")



		