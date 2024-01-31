# wapp to create a file  


import os
filename=input("enter file name")
if os.path.exists(filename):
	print(filename,"file already exists")
else:
	f= None
	try:
		filename=(filename, "w")
		print(filename , "created")
	except  Exception as e:
		print("issue ",e)
	finally:
		if f is not None:
			f.close()