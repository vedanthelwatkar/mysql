#waps to read list of integers from the user
#and print on the screen


marks=[]

res=input("do you want to enter marks y/n ")
while res=="y":
	score=input("enter your score ")
	marks.append(score)
	res=input("do you want to enter more ")

#method 1
print(marks)

#method 2
for m in marks:
	print(m)