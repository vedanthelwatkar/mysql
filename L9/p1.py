#wamdpp to maintain ipl teams names

team_names=set()
while True:
	op=int(input("1 add,2 remove,3 view,4 exit"))
	if op==1:
		name=input("enter team name ")
		r1=len(team_names)
		team_names.add(name)
		r2=len(team_names)
		if r2>r1:
			print(name, "name added ")
		else:
			print(name, "name already exists ")
	elif op==2:
		name=input("enter team name ")
		r1=len(team_names)
		team_names.discard(name)
		r2=len(team_names)
		if r1>r2:
			print(name , "name removed ")
		else:
			print(name, "does not exist ")
	elif op==3:
		print(team_names)
	elif op==4:
		break
	else:
		print("s i d u")
			