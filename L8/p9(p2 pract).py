#wapp to read list of marsk and print the lowest and highest marks

marks=[]

res=input("do you want to enter marks y/n ")
while res=="y":
	m=int(input("enter marks"))
	marks.append(m)
	res=input("do you want to enter more marks y/n ")

marks.sort()
low=marks[0]
high=marks[-1]
print(low,high)
print(min(marks))
print(max(marks))	
	
