queue=[]
while True:
	op=int(input("1 enqueue,2 dequeue, 3 show,4 exit = "))
	if op==1:
		ele=int(input("enter element "))
		queue.append(ele)
		print("the number enqueued is =",ele)
	elif op==2:
		if len(queue)==0:
			print("queue is empty")
		else:
			ele=queue.pop()
			print("the number dequeued is =",ele)
	elif op==3:
		print(queue)
	elif op==4:
		break
	else:
		print("i dont understand")
