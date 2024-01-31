from tkinter import *
from datetime import *
root = Tk()
root.geometry("600x400+600+200")
root.title("Mera Dusra Frame")
f= ("Courier",40,"bold")
root.configure(bg="lightyellow")

dt= datetime.now()
hr=dt.hour
msg =""
if hr < 12:
	msg =("Good Morning")
elif hr < 16 :
	msg =("Good Afternoon")
else:
	msg =("Good Evening")
lab=Label(root,text=msg,font=f,fg="red",bg="lightyellow")
lab.pack(pady=50)
root.mainloop()