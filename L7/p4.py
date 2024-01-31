#wapp to read list of numbers and count 
#1) no. of +ve   	#2) no. of -ve   	#3) no. of 0s'

num=[]

res=input("do you want to enter a number y/n ")
while res=="y":
	n=float(input ("enter  number "))
	num.append(n)
	res=input("do you want to enter more y/n ")

c1, c2, c3=0, 0, 0
for n in num:
	if n > 0.0:
		c1 = c1 + 1
	elif n < 0.0:
		c2 = c2 + 1
	elif n==0.0:
		c3 = c3 + 1

print(c1, c2, c3)