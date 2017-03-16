# 8.4 write a method to compute all permutations of a string
def permutation(s):
	n = len(s)
	l = list(s)
	if n == 1:
		return [l]
	elif n== 2:
		return [l, [l[1],l[0]]]
	elif n>2:
		l = []
		perm = permutation(s[:n-1])
		for i in range(n):
			for item in perm:
				l.append(item[:i] + [s[n-1]] + item[i:] )
		return l

		
		





s = 'pengkai'
print list(s)
print permutation(s)