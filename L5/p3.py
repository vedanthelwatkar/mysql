#wapp to read the radius from the user and print the area and circumference of circle

radius=float(input("enter radius "))
if radius >0:
	pi=3.14
	area=pi*radius**2
	circum=2*pi*radius
	print("area=",round(area,2))
	print("circum=",round(circum,2))
else:
	print("invalid input")