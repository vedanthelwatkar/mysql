#wapp to read list of marks and count
#1)m>80		#2)m>60		#3)m>40		
#4)others

#list declare
marks=[]

#list ke elements of read
res=input("do you want to enter some marks y/n ")
while res=="y":
	m=int(input("enter marks "))
	marks.append(m)
	res=input("do you want to enter more marks ")

#list ko process
c1,c2,c3,c4=0,0,0,0
for m in marks:
	if m>80:
		c1+=1
	elif m>60:
		c2+=1
	elif m>40:
		c3+=1
	else:
		c4+=1

print("c1=",c1)
print("c2=",c2)
print("c3=",c3)
print("c4=",c4)