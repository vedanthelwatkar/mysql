# wapp to delete a file


import os
filename=input("enter filename")
if os.path.exists(filename):
	os.remove(filename)
	print(filename. "removed")
else:
	print("file does not exists")

	