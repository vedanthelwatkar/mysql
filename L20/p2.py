import requests

try:
	wa = "https://api.quotable.io/random"
	res = requests.get(wa)
	print (res)
	data = res.json()
	print(data)
	content = data [ "content" ]
	print("content ==> " , content)
	author = data ["author"]
	print("author ==> ", author)
except Exception as e:
	print("issue  ",e)