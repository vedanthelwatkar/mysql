from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *

root=Tk()
root.title("What Next App")
root.geometry("1000x500+50+50")
f= ("Arial",40,"bold")
a=("Calibri",40,"bold","italic")


lab_name = Label(root,text="Enter name",font=f)
ent_name = Entry(root,font=f)
lab_name.place(x=50,y=50)
ent_name.place(x=350,y=50)
	

s=IntVar()
s.set(1)
lab_select = Label(root,text ="Select one",font=f)
rb_job = Radiobutton(root,text = "Job",font=a,var=s,value=1)
rb_ms = Radiobutton(root,text = "MS",font=a,var=s,value=2)
rb_mba = Radiobutton(root,text = "MBA",font=a,var=s,value=3)
lab_select.place(x=50,y=150)
rb_job.place(x=400,y=150)
rb_ms.place(x=400,y=250)
rb_mba.place(x=400,y=350)

def save():
	con=None
	try:
		con = connect("wb.db")
		cursor = con.cursor()
		sql = "insert into student values('%s','%s')"
		name = ent_name.get()
		choice = ""
		if s.get() == 1:
			choice="Job"
		elif s.get() == 2:
			choice="MS"
		else:
			choice="MBA"
		cursor.execute(sql % (name,choice))
		con.commit()
		showinfo("Success ! ", "THANK YOU")
	except Exception as e:
		con.rollback()
		showerror("Error !", e)
	finally:
		if con is not None:
			con.close()
		ent_name.delete(0,END)
		s.set(1)
		ent_name.focus()

btn_submit = Button(root,text="SUBMIT",font=a,command=save)
btn_submit.place(x= 650,y = 230)

root.mainloop()