
def isunique(s):
	a = [0 for i in xrange(256)]
	for l in s:
		if a[ord(l)] == 1: 
			return False
		a[ord(l)] ^= 1
	return True





a = 'abcdefgd'
print isunique(a)