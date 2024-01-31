import os
import pickle

class Student:
	def __init__(self,rno,name):
		self.rno=rno
		self.name=name
	
	def show(self):
		print("rno=", self.rno)
		print("name=", self.name)

#fn==>filename
#skd==> student ka data

fn="skd"

data={}	
if os.path.exists(fn):
	f=open(fn, "rb")
	data= pickle.load(f)	
	f.close()
	
while True:
	op=int(input("1 add, 2 show ,3 remove and 4 exit "))
	if op==1:
		rno=int(input("enter rno "))
		if data.get(rno) is None:
			name=input("enter name ")
			s=Student(rno,name)
			data[rno]=s	 
		else:
			print(rno, "already exists")
	elif op==2:
		for d in data:
			data[d].show()
			print("*" * 50)
	elif op==3:
		rno=int(input("enter rno "))
		if data.get(rno) is not None:
			data.pop(rno)
			print(rno," removed")
		else:
			print(rno," does not exist")
	elif op==4:
		f=open(fn, "wb")
		pickle.dump(data,f)
		f.close()
		break
	else:
		print("s i d u")