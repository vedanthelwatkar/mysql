#wapp to read an existing file
#with ==> ARM ( automatic resourse management )


import os
filename=input("enter filename ")
if os.path.exists(filename):
	f= None
	try:
		with open(filename,"r") as f:
			data= f.read()
			print(data)
	except Exception as e:
		print("issue",e)
else:
	print(filename,"file does not exists")