#wapp to write in a file

import os
filename=input("enter filename ")
if os.path.exists(filename):
	f= None
	try:
		f=open(filename, "a")
#		f=open(filename, "w")    --> all the existing data will be removed
		data=input("enter data to be put in the file ")
		f.write(data + "\n")
		print("file created and data is added to the file")
	except Exception as e:
		print("issue",e)
	finally:
		if f is not None:
			f.close()
	
else:

	print("file dose not exists ")