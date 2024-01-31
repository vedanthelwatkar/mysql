''' decorator: it is a function that takes as input another function and adds functonality to that function '''

def pretty(f):
	def inner():
		print("*" * 50)
		f()
		print("*" * 50)
	return inner

@pretty
def welcome():
	print("Good Morning")

@pretty
def bye():
	print("GoodBye")

welcome()
bye()