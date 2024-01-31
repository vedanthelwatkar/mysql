#waps to accept as input
#three numbers and receive
#their sum and avg

def compute(n1,n2,n3):
	sum= n1+n2+n3
	avg= sum / 3
	return sum,avg

n1= float(input("enter first number "))
n2= float(input("enter second number "))
n3= float(input("enter third number "))
sum,avg =compute(n1,n2,n3)
print("sum =", sum)
print("avg =", avg)
