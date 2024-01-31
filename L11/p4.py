class Person:
	def __init__(self,id,name,address):
		self.id=id
		self.name=name
		self.address=address
		
	def show(self):
		print("id =",self.id)
		print("name =",self.name)
		print("address =",self.address)
	
class Teacher(Person):
	def __init__(self,id,name,address,salary):
		super().__init__(id,name,address)
		self.salary=salary

	def show(self):
		super().show()
		print("salary =",self.salary)

class Hod(Teacher):
	def __init__(self,id,name,address,salary,dept):
		super().__init__(id,name,address,salary)
		self.dept=dept

	def show(self):
		super().show()
		print("dept =",self.dept)

t=Teacher(20,"neha","mulund",50000)
t.show()
print()
h=Hod(1,"amit","thane",50000,"Comps")
h.show()
