# waps to accept as input two integers 
#and return min of two

def minimum(n1,n2):
	if n1<n2:
		return n1
	else:
		return n2

n1= int(input("enter first integer "))
n2= int(input("enter second integer "))
res = minimum(n1,n2)
print("res =", res) 