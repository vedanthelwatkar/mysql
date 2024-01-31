#wapp to demo tuple

t1=()
print(t1,type(t1))

t2=(10,20,30,40)
print(t1,type(t2))

#t1.append(10) --> can't append in tuple
t1=t1+(10,)
print(t1)
#t1=t1+(10) --> tuple and int can't be concatinated

t2=t2+(20,)

print(t2)