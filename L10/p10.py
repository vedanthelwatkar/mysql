''' waoopp for class student
var: rno,name and marks
methods: __init__(),show(),findGrade()
m>80-->A
m>60-->B
m<60-->C
'''

class Student:
	def __init__(self,rno,name,marks):
		self.rno=rno
		self.name=name
		self.marks=marks

	def show(self):
		print("rno=",self.rno)
		print("name=",self.name)
		print("marks=",self.marks)

	def findGrade(self):
		if self.marks>80:
			print("Grade A")
		elif self.marks>60:
			print("Grade B")
		else:
			print("Grade C")

rno=int(input("enter rno. "))
name=input("enter your name ")
marks=int(input("enter marks "))
if marks >100:
	print("invalid input")
else:
	s=Student(rno,name,marks)
	s.show()
	s.findGrade()