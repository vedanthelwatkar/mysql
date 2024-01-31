#wapp to wish the user GM / GA / GE 

from datetime import *
dt= datetime.now()
hour = dt.hour
msg=""
if hour < 12:
	print("good morning")
elif hour < 16:
	print("good afternoon")
else:
	print("good evening") 