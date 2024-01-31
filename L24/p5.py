#generator==> it is a function which yeilds statement


def power_gen(m):
	n = 1
	while n <= m :
		yield 2 ** n
		n = n + 1

for i in power_gen(7):
	print(i)