from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *
from pymongo import * 
from datetime import *

root=Tk()
root.title("Enquiry App")
root.geometry("700x500+400+125")
f= ("Arial",30,"bold")
root.configure(bg="lightgreen")

lab_name = Label(root,text="Enter name",font=f,bg="lightsalmon",fg="white")
lab_name.pack(pady = 5)
ent_name = Entry(root,font=f,bg="skyblue",fg="white",bd=4)
ent_name.pack(pady=10)

lab_query = Label(root,text="Enter Query",font=f,bg="lightsalmon",fg="white")
lab_query.pack(pady=10)
st_query = ScrolledText(root,width=20,height=4,font=f,bg="skyblue",fg="white",bd=4)
st_query.pack()


def save():
	con= None
	try:
		con = MongoClient("mongodb://localhost:27017")
		db = con ["en29dec22"]
		coll = db ["enquiry"]
		name = ent_name.get()
		query = st_query.get(0.0,END)
		query = query.replace("\n","--")
		dt = datetime.now()
		info = {"name":name,"query":query,"en_dt":dt}
		coll.insert_one(info)
		showinfo("Success","We will get back to u")
	except Exception as e:
		showerror("Error", e)
	finally:
		if con is not None:
			con.close()

btn_submit = Button(root,text="SUBMIT",font=f,bg="lightsalmon",fg="white",command=save)
btn_submit.pack(pady=10)


root.mainloop()