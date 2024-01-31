#wapp to get info from : ipinfo.io

import requests
try:
	wa = "https://ipinfo.io/"
	res = requests.get(wa)
	print(res)
	data = res.json()
	print(data)
	city = data["city"]
	print("city name = ",city)
	state = data["region"]	
	print("state name = ",state)
	#print lat and lon on sep lines
	loc = data["loc"]
	abc = loc.split(",")
	lat = abc [0]
	lon = abc [1]
	print("latitude = ",lat )
	print("longitude = ",lon )

except Exception as e:	
	print("issue ",e)

	
	