# wapp to select student record

import mysql.connector
con = None
try:
	con = mysql.connector.connect(host = "localhost",user="root",password="abc123",database = "kc_6jan23")
	cursor = con.cursor()
	sql = "select * from student"
	cursor.execute(sql)
	data = cursor.fetchall()
	for d in data:
		print("rno = ",d[0], "name = ",d[1],"marks = ",d[2],"email = ",d[3])
except Exception as e:
	print("issue ",e)
finally:
	if con is not None:
		con.close()