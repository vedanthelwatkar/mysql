from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Mera Pehla Frame")
f= ("Arial Rounded",80,"bold")
lab = Label(root,text = "Good Morning",font=f,fg="red")
lab.pack(pady=100)
root.mainloop()
