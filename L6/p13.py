def add(*data):
	res=0
	for d in data:
		res = res + d

	print("res =" ,res)

add(10)
add(10,20)
add(10,20,30)
add(10,20,30,40)