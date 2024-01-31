#wapp to make a copy of file

import os
src_filename = input("enter source filename ")
if os.path.exists(src_filename):
	dest_filename= input("enter dest filename ")
	fsrc=None
	fdest=None
	try:
		fsrc = open(src_filename, "rb")
#		fsrc = open(src_filename, "r")	--> non binary files (.txt.py etc ) .docx not included
		fdest = open(dest_filename, "wb")
#		fdest = open(dest_filename, "w")	--> non binary files (.txt.py etc ) .docx not included
		data=fsrc.read()
		fdest.write(data)
		print("copy  completed")
	except Exception as e:	
		print("issue " , e)
	finally:
		if fsrc is not None:
			fsrc.close()
		if fdest is not None:
			fdest.close()
else:
	print(src_filename, "does not exists")