#wapp to update an emp record

from sqlite3 import *
con=None
try:
	con = connect ("kc.db")
	cursor = con.cursor()
	sql = "update emp set name = '%s' where id ='%d' "
	id=int(input("enter emp id "))
	name=intput("enter emp name ")
	cursor.execute(sql % (name,id))
	if cursor.rowcount==1:
		con.commmit()
		print("record created")
	else:
		print("record does not exists")
except Exception as e:
	con.rollback()
	print("issue ", e)
finally:
	if con is not None:
		con.close()