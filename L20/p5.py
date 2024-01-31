#wapp to create live USD to INR converter
#https://api.exchangerate-api.com/v4/latest/USD

import requests
try:
	wa = "https://api.exchangerate-api.com/v4/latest/USD"
	res = requests.get(wa)
#	print(res)
	data = res.json()
#	print(data)
	rates = data["rates"]["INR"]
	usd = float(input("Enter USD "))
	inr = usd * rates
	print("Inr = \u20b9",round(inr,2),sep = " ") 
#	print(rates)
	
except Exception as e:
	print("issue ",e)