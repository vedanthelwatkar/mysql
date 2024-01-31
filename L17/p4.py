#wapp to delete employee records

from sqlite3 import *
con = None
try:
	con= connect("kc.db")
	cursor = con.cursor()
	sel= "delete from emp where id = '%d' "
	id = int (input("enter emp id "))
	cursor.execute(sql % (id))
	if cursor.rowcount==1:
		con.commit()
		print("record created")
	else:
		print("record does not exists")
except Exception as e:
	print("issue ", e)
finally:
	if con is not None:
		con.close()