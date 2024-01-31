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

name = input("Enter your name")
feedback = input("Enter Feedback")
info = {"name":name,"feedback":feedback}

db.child("feedback").push(info)
print("Thanks for the feedback")