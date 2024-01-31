#wapp to read tuple of integers  from the user and print
#on the screen

data=()

#tuple read

res=input("do you want to enter data y/n ")
while res=="y":
	d=int(input("enter data "))
	data= data + (d,)
	res=input("do you want to enter more data y/n ")

#tuple display

print(data)

