# wapp to delete student record

from mysql.connector import *
con = None
try:
	con = connect(host = "localhost",user="root",password="abc123",database = "kc_6jan23")
	rno = int(input("Enter rno "))
	sql = "delete from student values where  rno = '%d' "
	cursor = con.cursor()
	cursor.execute(sql (rno))
	if cursor.rowcount == 1:
		print("Record Deleted")
	else:
		print("Record does not exists")
except Exception as e:
	if con is not None:
		con.rollback()
		print("issue ",e)
finally:
	if con is not None:
		con.close()