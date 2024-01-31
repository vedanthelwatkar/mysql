#wapp to read tuple of integers  from the user and print
#on the screen

values=()

val=input("do you want to enter integer y/n ")
while val=="y":
	d=int(input("enter data "))
	values = values + (d,)
	val=input("do you want to enter more data y/n ")

print(values)


