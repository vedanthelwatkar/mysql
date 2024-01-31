#waps to add three integers and print

def add(n1,n2,n3):
	print(n1,n2,n3)

#PP/POSITIONAL ARGUMENT
#add(10)					#miss u --> n2,n3
#add(10,20)				#miss u --> n3
add(10,20,30)

#KP/KEYWORD ARGUMENT
#add(n1=10,n2=30,n3=40)		
#add(n2=10,n1=30,n3=40)
#add(n1=10,n3=30,n2=40)

add (10,n2=20,n3=30)
#add(n1=10, 20 ,30)			#always first pa then ka