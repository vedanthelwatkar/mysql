''' wapp to add two numbers 
1)SP		2)POP		3)OOP
3)OOP
'''

class Addition:
	def __init__(self,n1,n2):
		self.n1=n1
		self.n2=n2

	def add(self):
		res=self.n1+self.n2
		print("res=",res)

n1=float(input("enter first no. "))
n2=float(input("enter second no. "))
a=Addition(n1,n2)
a.add()