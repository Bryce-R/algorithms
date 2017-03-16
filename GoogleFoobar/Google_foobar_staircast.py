def f(n,m,memo):
	#print n,m
	if m>n/2 or (m== n/2 and n%2 ==0):
		return 0
	elif (n,m) in memo:
		return memo[(n,m)]
	else:
		s = 1
		for i in xrange(m+1, (n-m)/2+1):
			s += f(n-m,i,memo)
		memo[(n,m)] = s
		return s

def answer(n):
	s = 0;
	memo = {(2,1):1, (3,1):1, (5,1):1, (5,2):1, (6,2) :1};
	for i in xrange(1,n/2+1):
		s+= f(n,i,memo)
	return s;

n = 200;
print answer(n)

