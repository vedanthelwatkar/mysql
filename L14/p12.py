#wapp to find the  current day
#and print if its weekday or weekend


from datetime import *
dt= datetime.now()
w= dt.strftime("%a")
print(w)

match w:
	case"Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
		print("its a weekday")
	case _:
		print("its a weekend") 