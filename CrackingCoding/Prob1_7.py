# set a M*N matrix's row and column to 0 if it has 0 in it
def setzero(l,m,n):
	row = []
	col = []
	for i in xrange(m):
		for j in xrange(n):
			if l[i][j] == 0:
				row.append(i)
				col.append(j)

	for i in row:
		for j in xrange(n):
			l[i][j] = 0
	for j in col:
		for i in xrange(m):
			l[i][j] = 0

# 1.8 determine if s2 is a rotation of s1 by calling substring only once
def isRotation(s1,s2):
	if len(s1) == len(s2):
		s1s1 = s1+s1
		if s2 in s1s1:
			return True
		else:
			return False
	else: return False



l = [[10, 5, 6, 8, 0, 9], [11, 0, 6, 25, 0, 9], [2, 7, 6, 8, 7, 9], [6, 5, 6, 8, 2, 9]]
m = len(l)
n = len(l[0])
for row in l:
	print row
print 'After'
setzero(l,m,n)
for row in l:
	print row

s1 = 'stephcurry'
s2 = 'currysteph'
print isRotation(s1,s2)