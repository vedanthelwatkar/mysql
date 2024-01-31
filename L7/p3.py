#waps to read list of marks
#print sum and avg of marks

marks=[]

res=input("do you want to enter your marks y/n ")
while res=="y":
	score=int(input("enter your score "))
	marks.append(score)
	res =input("do you want to enter more y/n ")

sum,avg=0.0,0.0
for m in marks:
	sum = sum + m

avg=sum / len(marks)

print("sum= ", sum)
print("avg =", avg)

