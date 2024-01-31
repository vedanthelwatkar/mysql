class Employee:
	def __init__(self,id,name,salary):
		self.id=id
		self.name=name
		self.salary=salary
	
	def show(self):
		print("id=",self.id)
		print("name=",self.name)
		print("salary=",self.salary)

	def bonus(self):
		ta=0.0
		if self.salary>=50000:
			ta= self.salary*0.20		
		else:
			ta=self.salary*0.10
		print("bonus generated =",ta)

class SalesPerson(Employee):
	def __init__(self,id,name,salary,comm):
		super().__init__(id,name,salary)
		self.comm=comm
	
	def show(self):
		super().show()
		print("comm =",self.comm)

s= Employee(10,"amit",10000)
s.show()
print("*" * 50)
sp=SalesPerson(1,"mithun",1500,800)
sp.show()