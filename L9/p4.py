#wapp to implement a simple chatbox

conv={
	"hello":"hi",
	"hi":"hello",
	"bye":"bye",
	"good morning":"good morning",
	"how are you":"fine",
	"classes":"kamal classes",
	"django":"feb 23",
	"fees":"8500",
	"discount":"no discount",
}

while True:
	qes=input("enter your question and press 4 to exit ")
	if qes=="4":
		break
	elif conv.get(qes) is not None:
		print(conv.get(qes))
	else:
		print("s i d u")
	