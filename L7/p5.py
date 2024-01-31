#wamdpp to implement DS: Stack/LIFO

stack=[]
while True:
	op=int(input("1 push,2 pop,3 show,4 exit = "))
	if op==1:
		ele=int(input("enter element "))
		stack.append(ele)
		print(ele,"is pushed on the stack ")
	elif op==2:
		if len(stack)==0:
			print("stack is empty ")
		else:
			ele=stack.pop()
			print("popped element =",ele)
	elif op==3:
		print(stack)
	elif op==4:
		break
	else:
		print("sorry i don't understand ")


