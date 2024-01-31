#wapp to write in a file

import os
filename=input("enter filename ")
if os.path.exists(filename):
	f= None
	try:
		filename=(filename,"a")
		data=input("enter data to be entered in the file")
		f.write(data + \n)
	except Exception as e:
		print("issue ",e)
	finally:
		if f is not None:
			f.close()
else:
	print("filename does not exists")