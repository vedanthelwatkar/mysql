'''wapp to maintain list of names of students who will
attend the party CURD/CRUD'''

names=[]

while True:
	print("choose any number")
	op=int(input("1 new,2 remove,3 view,4 exit= "))
	if op==1:
		n=input("enter your name")
		names.append(n)
		print("your name has been added")
	elif op==2:
		n=input("enter your name")
		if n in names:
			names.remove(n)
			print("your name has been removed")
		else:
			print("your name is not in the list")
	elif op==3:
		print(names)
	elif op==4:
		break
	else:
		print("s i d u")