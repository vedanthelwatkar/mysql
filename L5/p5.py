#wapp to read an integer and print its table


num=int(input("enter a +ve integer "))
if num > 0:
	i=1
	ans=0
	while i <=10:
		ans=num*i
		print(num,"*",i,"=",ans)
		i=i+1
else:
	print("invalid input")