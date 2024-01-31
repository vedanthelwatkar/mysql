# wapf to accept as input length and breadth
# and return area and perimeter of rectangle

def compute(length,breadth):
	area= length * breadth
	peri= 2 * (length + breadth)
	return area,peri

length=float(input("enter length "))
breadth=float(input("enter breadth "))
if (length>0.0) and (breadth> 0.0):
	area,peri= compute(length,breadth)
	print("area = ", round(area,2))
	print("peri = ", round(peri,2))
else:
	print("invalid input")