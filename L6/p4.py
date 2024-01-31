#waps to accept as input two
#integers and print their addn

def add(n1, n2):
	res=(n1+ n2)
	return res

n1=int(input("enter first number "))
n2=int(input("enter second number "))
res=add(n1, n2)
print("res of addn = ", res)