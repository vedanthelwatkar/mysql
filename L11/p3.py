#simple/single inheritence

class Person:
	def __init__(self,id,name,address):
		self.id=id
		self.name=name
		self.address=address

	def show(self):
		print("id=",self.id)
		print("name=",self.name)
		print("address=",self.address)


class Student(Person):
	def __init__(self,id,name,address,marks):
		super().__init__(id,name,address)
		self.marks=marks

	def show(self):
		super().show()
		print("marks=",self.marks)

s=Student(10,"amit","thane",50)
s.show()