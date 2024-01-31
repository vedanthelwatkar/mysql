# iterator --> these are objects that can be iterated upon 

s1 = "anusha"
print(s1)

for s in s1:
	print(s , end="")
print()

it1 = iter(s1)
for i in it1:
	print(i,end ="")
print()
