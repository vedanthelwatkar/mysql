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

data={}
while True:
	op=int(input("1 add,2 show,3 remove,4 exit "))
	if op==1:
		rno=int(input("enter rno "))
		if data.get(rno) is None:
			name=input("enter your name ")
			marks=int(input("enter your marks "))
			s= Student(rno,name,marks)
			data[rno]=s
		else:
			print(rno, " already exists " )
	elif op==2:
		for d in data:
			data[d].show()
			print("*" * 50)
	elif op==3:
		rno=int(input("enter rno "))
		if data.get(rno) is None:
			print(rno, " is not present ")
		else:
			data.pop(rno)
			print(rno, " is removed ")			
	elif op==4:
		break
	else:
		print(" s i d u ")
















