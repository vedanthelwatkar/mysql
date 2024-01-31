from tkinter import *
from tkinter.messagebox import *

root= Tk()
root.title("Square root finder")
root.geometry("1000x500+250+125")

f= ("Calibri", 40 , "bold")

def find():
	try:
		s=ent_num.get()
		n=float(s)
		if n < 0.0:
			raise ValueError
		r= n * n
		r=round(r,2)
		msg= "Square = "  + str(r)
		showinfo("Jawaab",msg)
	except ValueError:
		showerror("Galat Kiya","number only")
		ent_num.delete(0,END) 		

lab_num=Label(root,text="Enter number",font=f)
ent_num=Entry(root,font=f)
btn_find=Button(root,text="Find Square",font=f,command=find)
lab_num.place(x=50,y=30)
ent_num.place(x=400,y=30)
btn_find.place(x=350,y=150)
root.mainloop()