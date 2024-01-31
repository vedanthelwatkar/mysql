#wapp to delete an existing file

import os
filename=input("enter filename ")
if os.path.exists(filename):
	os.remove(filename)
	print(filename,"file removed ")
else:
	print("file dose not exists ")