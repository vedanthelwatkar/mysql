class Graph:
	def __init__(self):
		self.info = {}
		
	def add(self,start,end):
		if start in self.info:
			self.info[start].append(end)
		else:
			self.info[start] = [end]
	
	def show(self):
		for i in self.info:
			print("NODE",i)
			for j in self.info[i]:
				print(i,"-",j)
	
	def bfs(self,node):
		visited = [node]
		queue = [node]
		while queue:	
			s = queue.pop(0)
			print(s,end = " ")
			if s in self.info.keys():
				for n in self.info[s]:
					if n not in visited:
						visited.append(n)
						queue.append(n)

g = Graph()
while True:
	op = int(input("1 add,2 show, 3 exit ,4 bfs "))	 
	if op == 1:
		start = input("enter start node ")
		end = input("enter end node ")
		g.add(start,end)
	elif op == 2:
		g.show()
	elif op ==  3:
		break
	elif op == 4:
		start = input("Enter start")
		g.bfs(start)
	else:
		print("s i d u")

