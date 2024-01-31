from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *

root = Tk()
root.title("success story app")
root.geometry("600x600+50+50")
f= ("Arial",30,"bold")

def save():
	con= None
	try:
		con = connect("ss.db")
		cursor = con.cursor()
		sql = " insert into student values('%s','%s','%f')"
		name=ent_name.get()
		company=ent_company.get()
		package= float(ent_package.get())
		cursor.execute(sql % (name,company,package))
		con.commit()
		showinfo("Success !","Record Created")
	except Exception as e:
		con.rollback()
		showerror("Galat Kiya", e)
	finally:
		if con is not None:
			con.close()	
		ent_name.delete(0,END)
		ent_company.delete(0,END)
		ent_package.delete(0,END)
		ent_name.focus()
	
lab_name= Label(root,text ="Enter name",font=f)
ent_name=Entry(root,font=f)
lab_company=Label(root,text="Enter company",font=f)
ent_company=Entry(root,font=f)
lab_package=Label(root,text="Enter package",font=f)
ent_package=Entry(root,font=f)
btn_submit=Button(root,text="Submit",font=f,command=save)


lab_name.pack(pady=10)
ent_name.pack(pady=10)
lab_company.pack(pady=10)
ent_company.pack(pady=10)
lab_package.pack(pady=10)
ent_package.pack(pady=10)
btn_submit.pack(pady=10)

root.mainloop()
