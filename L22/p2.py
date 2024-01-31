from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyDJjkShQJxPAUn-BRuDYKurmO2Ac06tZD4",
  "authDomain": "feedbackpython3jan23-68815.firebaseapp.com",
  "databaseURL": "https://feedbackpython3jan23-68815-default-rtdb.firebaseio.com",
  "projectId": "feedbackpython3jan23-68815",
  "storageBucket": "feedbackpython3jan23-68815.appspot.com",
  "messagingSenderId": "488226807651",
  "appId": "1:488226807651:web:b624fb21396a4bf83f7d56"
};

fb = pyrebase.initialize_app(firebaseConfig)
db = fb.database()

root = Tk()
root.title("Feeback App by KS")
root.geometry("500x600+50+50")

f= ("Arial",30,"bold","italic")
lab_name = Label(root, text="Enter name",font=f)
lab_name.pack()
ent_name = Entry(root,font=f,bd=4)
ent_name.pack()

lab_fb = Label(root,text="Enter feedback",font=f)
lab_fb.pack()
st_fb = ScrolledText(root,font=f,height=5)
st_fb.pack()

def save():
	name = ent_name.get()
	feedback = st_fb.get("1.0",END)
	info = {"name":name,"feedback":feedback}
	db.child("feedback").push(info)
	showinfo("Success!","Thanks for the feedback")
	ent_name.delete(0,END)
	st_fb.delete("1.0",END)
	ent_name.focus()

btn_submit = Button(root,text="Submit",font=f,command=save)
btn_submit.pack(pady=10)

root.mainloop()