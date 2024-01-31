from tkinter import *

root = Tk()
root.title("square root finder")
root.geometry("1000x500+250+125")
f=("Arial",40,"bold","italic")
a=("Calibri",40,"bold")


lab_num=Label(root,text ="enter number",font=f)
ent_num=Entry(root,font=f)
lab_num.place(x="30",y="50")
ent_num.place(x="400",y="50")

def find():
	try:
		s=ent_num.get()
		n=float(s)
		if n < 0.0:
			raise ValueError()
		r= n ** 0.5
		r= round(r,2)
		msg= ("square root = " ) + str(r)		
		lab_ans.configure(text=msg)
	except ValueError:
		lab_ans.configure(text="+ve integers only")


btn_find=Button(root,text="Find square root",font=a,command=find)
btn_find.place(x="300",y="150")
lab_ans=Label(root,font=f)
lab_ans.place(x="250",y="350")

root.mainloop()