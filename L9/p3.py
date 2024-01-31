data={"maharashtra":"mumbai","kerela":"trivandrum","goa":"panjim","bihar":"patna","gujrat":"gandhinagar"}

while True:
	op=int(input("1 search and 4 exit"))
	if op==1:
		sn=input("enter state name ")
		cn=data.get(sn)
		if cn is None:
			print("not available")
		else:
			print(cn)
	elif op==4:
		break
	else:
		print(" s i d u ")