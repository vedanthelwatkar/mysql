class Employee:
	def __init__ (self,name,salary):
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
while True:
	op=int(input("1 add,2 show,3 remove,4 exit "))
	if op==1:
		id=int(input("enter id "))
		if data.get(id) is None:
			name=input("enter name ")
			salary=float(input("enter salary "))
			e=Employee(name,salary)
			data[id]=e
			print(id, " created ")
		else:
			print(id, " already exists ")
	elif op==2:
		for d in data:
			print("id=",d)
			data[d].show()
			data[d].computeTax()
			print("*" * 50)
	elif op==3:
		id=int(input("enter emp id "))
		if data.get(id) is not None:
			data.pop(id)
			print(id, " is removed ")
		else:
			print(id, " does not exist ")
	elif op==4:
		break
	else:
		print(" s i d u ")