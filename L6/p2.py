#wapf to chant some mantras

def chant():
	print("hare rama")
	print("hare krishna")
	print("hare hare")

num=int(input("enter a +ve integer "))
if num >0:
	for i in range(1,num+1):
		chant()
else:
	print("invalid input")