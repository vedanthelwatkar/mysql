#wapp to demo datetime

from datetime import *
dt=datetime.now()
print(dt)
d=datetime.now().date()
print(d)
t=datetime.now().time()
print(t)

print(dt.day)
print(dt.month)
print(dt.year)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)