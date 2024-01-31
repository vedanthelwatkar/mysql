#wapp to create  new file

import os
filename=input("enter filename ")
if os.path.exists(filename):
	print(filename, " already exists")
else:
	f= None
	try:
		f= open(filename, "w")
		print(filename," created")
	except Exception as e:
		print("issue",e)
	finally:
		if f is not None:
			f.close()