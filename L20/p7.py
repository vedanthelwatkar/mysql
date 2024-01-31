
import requests
try: 
	a1 = "https://api.openweathermap.org/data/2.5/weather"
	a2 = "?q=" + input("enter city name ")
	a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
	a4 = "&units=" + "metric"
	wa = a1 + a2 + a3 + a4
	res = requests.get(wa)
	data = res.json()
	ans = data ["main"]["temp"]
	print("temp = ",ans) 
except Exception as e:
	print("issue ",e)