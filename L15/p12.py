from tkinter import *
from random import *

root = Tk()
root.title("Random Motivation msg Generator")
root.geometry("1000x500+250+125")


def gen():
	quote=["you can do it","you are the best","you are a champion","you can do it","push harder","get your shit together","lessgo champ","python is fun "]
	r=randrange(len(quote))
	lab.configure(text=quote[r])

f=("Arial",50,"bold")
root.configure (bg="yellow")
btn=Button(root,text="GET QUOTE",font=f,command=gen)
btn.pack(pady=20)
lab=Label(root,text="",font=f)
lab.pack(pady=20)
root.mainloop()