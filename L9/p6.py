class circle:
	def __init__(self,radius):
		self.radius=radius

	def show(self):
		print("radius= ",self.radius)

	def area(self):
		res=3.1415 * self.radius ** 2
		print("area = ", round(res,2))

	def circumference(self):
		res=2 ** 3.14159 * self.radius
		print("circumference =",round(res,2))

c1=circle(4.6)
c1.show()
c1.area()
c1.circumference()
		
c2=circle(5.6)
c2.show()
c2.area()
c2.circumference()