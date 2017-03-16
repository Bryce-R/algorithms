# 8.1 nth fibbonaci number
def fib(n):
	a,b = 1, 1
	if n <=0:
		return False
	elif n == 1 and n ==2:
		return 1
	else:
		for i in xrange(3,n+1):
			c = a + b
			a,b = b,c
		return c

def fib_r(n):
	if n == 1 or n== 2:
		return 1
	else:
		return fib_r(n-1)+fib_r(n-2)

n = 6
print fib(n)
print fib_r(n)