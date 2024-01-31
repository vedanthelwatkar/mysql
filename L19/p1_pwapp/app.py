from tkinter import  *
from tkinter.messagebox import *
from pymongo import *
from datetime import *


root= Tk()
root.title("Pizza Wallah")
root.geometry("1000x600+250+125")
root.iconbitmap("pizza.ico")
f= ("Arial",30,"bold","italic")


lab_name = Label(root,text="Enter Name",font=f)
lab_name.place(x=50,y=50)
ent_name = Entry(root,font=f)
ent_name.place(x=400,y=50)


lab_size = Label(root,text="Size",font=f)
lab_size.place(x=50,y=150)

s=IntVar()
s.set(2)
rb_sm = Radiobutton(root,text="Small",font=f,var=s,value=1)
rb_me = Radiobutton(root,text="Medium",font=f,var=s,value=2)
rb_la = Radiobutton(root,text="Large",font=f,var=s,value=3)

rb_sm.place(x=300,y=150)
rb_me.place(x=500,y=150)
rb_la.place(x=750,y=150)

lab_topp = Label(root,text="Toppings",font=f)
lab_topp.place(x=50,y=250)

to,on,ca,ch=IntVar(),IntVar(),IntVar(),IntVar()

cb_to = Checkbutton(root,text="Tomato",font=f,variable=to)
cb_on = Checkbutton(root,text="Onion",font=f,variable=on)
cb_ca = Checkbutton(root,text="Capsicum",font=f,variable=ca)
cb_ch = Checkbutton(root,text="Cheese",font=f,variable=ch)
cb_to.place(x=300,y=250)
cb_on.place(x=600,y=250)
cb_ca.place(x=300,y=350)
cb_ch.place(x=600,y=350)

def save():
	con= None
	try:
		con = MongoClient("mongodb://localhost:27017")
		db = con ["pw29dec22"]
		coll = db["pizza_orders"]

		name = ent_name.get()
		size = ""
		if s.get() == 1:
			size = "Small"
		elif s.get() == 2:
			size = "Medium"
		else:
			size = "Large"
		
		toppings = ""
		if to.get() == 1:
			toppings += "Tomato"
		if on.get() == 2:
			toppings += "Onion"
		if ca.get() == 3:
			toppings += "Capsicum"
		if ch.get() == 4:
			toppings += "Cheese"
		
		dt = datetime.now()
		
		info = {"name":name,"size":size,"toppings":toppings,"dt":dt}
		
		coll.insert_one(info)
		showinfo("Success","ORDER PLACED")

	except Exception as e:
		showerror("Issue", e)
		ent_name.delete(0,END)
		s.get(2)
		to.set(0)
		on.set(0)
		ca.set(0)
		ch.set(0)
		ent_name.focus()
		
	finally:	
		if con is not None:
			con.close()

btn_order = Button(root,text="Place Order",font=f,command=save)
btn_order.place(x=400,y= 450)

root.mainloop()