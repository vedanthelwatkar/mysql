#wapp to maintain list of names of students who will
#attend the party		CURD/CRUD

#list declare
names=[]

while True:
	print("choose any number")
	op=int(input("1 new,2 remove,3 show,4 exit = "))
	if op==1:
		n=input("enter your name ")
		names.append(n)
		print("name registered")
	elif op==2:
		n=input("enter your name ")
		if n in names:
			names.remove(n)
			print(n,"name removed")
		else:
			print(n,"name not registered")
	elif op==3:
		print(names)
	elif op==4:
		break
	else:
		print("s i d u")