#wapp to get BTC using cui app
#https://api.coindesk.com/v1/bpi/currentprice.json

import requests

try:
	wa =  "https://api.coindesk.com/v1/bpi/currentprice.json"
	res = requests.get(wa)
	data = res.json()
#	print(data)
	ans = data["bpi"]["USD"]["rate"]
	print(ans)
	
except Exception as e:
	print("issue ",e)