#waps to accept as input radius
#and print area and circum of cicrle


def compute(radius):
	pi=3.14159
	area= pi*radius**2
	circum=2*pi*radius
	print("area = ", round(area,2))
	print("circum = ", round(circum,2))

radius= float(input("enter radius "))
if radius > 0:
	compute(radius)
else:
	print("invalid radius")