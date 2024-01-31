#class ==> encapsulation

class student:
	def __init__(self,rno,name,marks):
		self.rno=rno
		self.name=name
		self.marks=marks

	def show(self):
		print("rno= ",self.rno)
		print("name= ",self.name)
		print("marks= ",self.marks)

#object==> instantiation
s1= student(10,"amit",90)
s1.show()

s2=student(11,"neha",87)
s2.show()