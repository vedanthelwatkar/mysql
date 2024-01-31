#wapp to check if this year is leap year or not

from datetime import *
dt = datetime.now()
year = dt.year

if year %4 :
	print("the year is a leap year")
else:
	print("the year is not a leap year")
	 