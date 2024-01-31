from tkinter import *
from random import * 

root = Tk()
root.title=("Color me app  by KS")
root.geometry=("800x500+100+00")
f= ("Arial",50,"bold","italic")

def change():
	colors = ["red","pink","green","yellow","blue","black","white","orange"]
	r=randrange(len(colors))
	root.configure(bg=colors[r])

btn = Button(root,text="Mohe Rang De",font=f,command=change)
btn.pack(pady=100)
root.mainloop()