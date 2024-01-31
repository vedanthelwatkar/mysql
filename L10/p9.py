'''
waopp for class Circle:
var:			Radius
methods		__init__(),show(),area(),circumference()
'''

class Circle:
	pi=3.14159
	def __init__(self,radius):
		self.radius=radius
	def show(self):
		print("radius=",self.radius)
	def area(self):
		res= Circle.pi * self.radius **2
		print("area=",round(res,2))
	def circumference(self):
		res=2 * Circle.pi *self.radius
		print("circumference=",round(res,2))

radius=float(input("enter radius "))
if radius >= 0.0:
	c= Circle(radius)
	c.show()
	c.area()
	c.circumference()
else:
	print("invalid radius ")
	