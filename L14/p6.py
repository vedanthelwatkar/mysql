#  wapp to find square root of given no

import math
try:
	num=float(input("enter number "))
	if num > 0.0:
		res= math.sqrt(num)
		print("res=",round(res,2))
	else:
		print("invalid input")
except:
	print("enter a +ve number")
