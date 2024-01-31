#wapp to find factorial of a given integer
#5		1*2*3*4*5=120

num=int(input("enter a positive integer "))
if num > 0 :
	factorial=1
	i=1
	for i  in range(1,num+1):
		factorial=factorial*i
	print("factorial = ", factorial)
else:
	print("invalid input")