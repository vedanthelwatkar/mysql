class Queue:
	def __init__(self):
		self.data = []
	def enq(self,ele):
		self.data.append(ele)
		print(ele, " is inserted into the queue")
	def deq(self):
		if len(self.data) == 0:
			print("queue empty")
		else:
			ele = self.data.pop()
			print("popped element =  ",ele)
	def show(self):
		print(self.data)

q =Queue()
while True:
	op= int(input("1 enq ,2 deq, 3 show, 4 exit "))
	if op ==1:
		ele= int(input("enter element"))
		q.enq(ele)
	elif op == 2:
		q.deq()
	elif op == 3:
		q.show()
	elif op == 4:
		break
	else:
		print("s i d u")
	