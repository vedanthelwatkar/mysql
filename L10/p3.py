'''wapp to checck even/odd numbers using 
1) SP		2)POP		3)OOP
3) OOP
'''

class EvenOdd:
	def __init__(self,num):
		self.num= num

	def check(self):
		if self.num % 2 ==0:
			print("even")
		else:
			print("odd")

num=int(input("enter integer "))
e= EvenOdd(num)
e.check()