#wapp to read radius from the user and print 
#area and circumference of circle


from math import *
radius=float(input("enter radius "))
try:
	if radius > 0.0:
		area= pi * pow(radius,2) 
		circumference = 2 * pi * radius
		print("area= ", round(area,2))
		print("circumference = ", round(circumference,2))
	else:
		print("invalid input")
except Exception as e:
	print("issue ",e)