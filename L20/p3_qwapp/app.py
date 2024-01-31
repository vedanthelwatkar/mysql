from tkinter import *
from tkinter.messagebox import *
import requests

root =  Tk()
root.title("Quotes Wallah App")
root.geometry("850x600+250+125")
f= ("Arial",30,"bold") 


lab_quotes=Label(root,text="Click on submit to get random quotes!!!",font=f)
lab_quotes.pack(pady = 10)

def get():
	try:
		wa = "https://api.quotable.io/random"
		res = requests.get(wa)
		print (res)
		data = res.json()
		print(data)
		content = data [ "content" ]
		lab_msg.configure(text=content)
		
	except Exception as e:
		print("issue ",e)
		


btn_get= Button(root,text="GET QUOTES",font=f,command = get)
btn_get.pack(pady = 50)
lab_msg = Label(root,text="",font=f,wraplength=500)
lab_msg.pack(pady=20)



root.mainloop() 