from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

def f1():
	root.withdraw()
	aw.deiconify()

def f2():
	aw.withdraw()
	root.deiconify()	
	
def f3():
	root.withdraw()
	vw.deiconify()
	vw_sc.delete(1.0,END)
	con = None
	try:
		con = connect("kc.db")
		cursor = con.cursor()
		sql = "select * from student order by rno"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + "rno = " + str(d[0]) + " name = " + str(d[1]) + "\n"
		vw_sc.insert(INSERT,info)
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:	
			con.close()
		
def f4():
	vw.withdraw()
	root.deiconify()

def f5():
	con = None
	try:
		con = connect("kc.db")
		cursor = con.cursor()
		sql = "insert into student values('%d','%s')"
		rno = int(aw_ent_rno.get())
		name = aw_ent_name.get()
		cursor.execute(sql%(rno,name))
		con.commit()
		showinfo("Success!","Record Created")
	except Exception as e:
		con.rollback()
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
		aw_ent_rno.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_rno.focus()
	

root = Tk()
root.title ("S.M.S app")
root.geometry("500x600+50+50")
f= ("Calibri",30,"bold")

add_btn= Button(root,text="Add Students",font=f,command = f1,width=15)
view_btn= Button (root,text="View Students",font=f,command=f3,width=15)
add_btn.pack(pady=20)
view_btn.pack(pady=20)

aw = Toplevel(root)
aw.title("Add Students")
aw.geometry("500x600+50+50")

aw_lab_rno = Label(aw,text="Enter rno",font=f)
aw_ent_rno = Entry(aw,font=f,bd=2)
aw_lab_name = Label(aw,text="Enter name",font=f)
aw_ent_name = Entry(aw,font=f,bd=2)
aw_btn_save= Button(aw,text="Save",font=f,command = f5)
aw_btn_back = Button(aw,text="Back",font=f,command = f2)
aw_lab_rno.pack(pady=10)
aw_ent_rno.pack(pady=10)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)

def f7(event):
	f5()
aw_btn_save.bind("<Return>",f7)

aw.withdraw()

vw = Toplevel(root)
vw.title("View Students")
vw.geometry("500x600+50+50")
vw_sc = ScrolledText(vw,font=f,width=22,height=7)
vw_btn_back = Button(vw,text="Back",font=f,command = f4)
vw_sc.pack(pady=20)
vw_btn_back.pack(pady=20)
vw.withdraw()

def f6():
	answer = askyesno(title='confirmation',message='do you really want to exit?')
	if answer:
		root.destroy()

root.protocol("WM_DELETE_WINDOW",f6)
root.mainloop()