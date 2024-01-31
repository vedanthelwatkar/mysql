#wapp to read rating from 1 to 5 and print msg
#5/4= good 				#3/2=meh 				#1=poor

rating=int(input("enter rating "))
if (rating<1) or (rating>5):
	print("invalid input")
elif (rating==5) or (rating==4):
	print("good")
elif (rating==3) or (rating==2):
	print("meh")
else:
	print("poor")


