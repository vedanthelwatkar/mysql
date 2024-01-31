#wapp to read a file and add data



import os
filename=input("enter filename ")
if os.path.exists(filename):
	f= None
	try:
		f=open(filename, "r")
		data= f.read()
		print(data)
	except Exception as e:
		print("issue ",e)
	finally:
		if f is not None:
			f.close()
else:
	print("filename does  not exists")