from mysql.connector import *

con = None
try:
	con = connect(host = "localhost",user = "root",
	password =  "abc123", database = "kc_6jan23")
	rno = int(input("Enter rno "))
	name = input("Enter Name ")
	marks = int(input("Enter Marks "))	
	email = input("Enter Email ")
	cursor = con.cursor()
	sql = "insert into student values ('%d','%s','%d','%s') "
	cursor.execute(sql % (rno,name,marks,email))
	con.commit()
	print("Record Created")
except Exception as e:
	if con is not None:
		con.rollback()
		print("issue ",e)
finally:
	if con is not None:
		con.close()
