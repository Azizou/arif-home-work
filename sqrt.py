import math
def sqrt(n):
	root = n/2
	r = x = 0
	s = input('Enter a value for the number of runs:')
	s = int(s)
	while x < s:
		r = n/root
		root = (root + r)/2
		x += 1
	print(root)
	print(root - math.sqrt(n))


def sqrt2(n):
	rac = n/2
	r = 0
	s = input('Enter a value for the number of runs:')
	s = int(s)
	for x in range(s):
		r = n/rac
		rac = (rac + r)/2
	print(rac)
n = eval(input('N:'))
sqrt(n)
sqrt2(n)