#wapp to create file downloader

import requests
try:
	wa = input("Enter URL ")
	res = requests.get(wa)
	print(res)
	fn = input("Enter filename ")
	f = open(fn, "wb")
	f.write(res.content)
	f.close()
	print("download complete") 
except Exception as e:
	print("issue ",e)
