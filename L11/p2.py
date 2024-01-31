class Employee:
	def __init__(self,id,name,salary):
		self.id=id
		self.name=name
		self.salary=salary

	def show(self):
		print("id =",self.id)
		print("name =",self.name)
		print("salary =",self.salary)

	def computeTax(self):
		ta=0.0
		if self.salary > 50000:
			ta=self.salary * 0.20
		else:
			ta=self.salary * 0.10
		print("tax amount = ",ta)

class SalesPerson(Employee):
	def __init__(self,id,name,salary,comm):		
		super().__init__(id,name,salary)
		self.comm=comm
	
	def show(self):
		super().show()
		print("comm =",self.comm)

s=SalesPerson(10,"amit",5000,100)
s.show()
s.computeTax()
