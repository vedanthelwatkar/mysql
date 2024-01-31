#wapp to read the list of marks and print the highest and lowest marks

marks=[]
res=input("do you want to enter marks y/n ")
while res=="y":
	m=int(input("enter marks "))
	marks.append(m)
	res=input("do you want to enter more marks y/n ")

#method 1--> (sort)

marks.sort()
low=marks[0]
high=marks[-1]
print(low,high)

#method 2--> (min & max)
low=min(marks)
high=max(marks)
print(low,high)



	