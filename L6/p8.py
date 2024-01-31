#waps to accept as input radius
#and return area and circum of cicrle


def compute(radius):
	pi=3.14159
	area= pi*radius**2
	circum=2*pi*radius
	return area,circum

radius= float(input("enter radius "))
if radius > 0:
	area ,circum=compute(radius)
	print("area = ", round(area,2))
	print("circum = ", round(circum,2))
else:
	print("invalid radius")