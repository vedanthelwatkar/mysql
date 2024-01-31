from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd

root= Tk()
root.title("Score")
root.geometry("600x500+50+50")
f = ("Arial",30,"bold")

lab_name=Label(root,text="Enter Name",font=f)
lab_name.pack()
ent_name=Entry(root,font=f)
ent_name.pack()

lab_phy=Label(root,text="Enter phy marks",font=f)
lab_phy.pack()
ent_phy=Entry(root,font=f)
ent_phy.pack()

lab_chem=Label(root,text="Enter chem marks",font=f)
lab_chem.pack()
ent_chem=Entry(root,font=f)
ent_chem.pack()

lab_maths=Label(root,text="Enter maths marks",font=f)
lab_maths.pack()
ent_maths=Entry(root,font=f)
ent_maths.pack()

def gc():
	name = ent_name.get()
	phy= ent_phy.get()	
	chem=ent_chem.get()
	maths=ent_maths.get()
	subjects=["phy","chem","maths"]
	marks=[phy,chem,maths]
	plt.plot(subjects,marks,linewidth=4,marker="o",markerfacecolor="red")
	plt.xlabel("Subjects")
	plt.ylabel("Marks")
	plt.title(name + "'s score")
	plt.grid()
	plt.show()
	plt.savefig(name + "'s score.pdf")
	plt.savefig(name + "'s score.png")

	

btn_score=Button(root,text ="Generate Score",font=f,command=gc)
btn_score.pack(pady=10)

root.mainloop()