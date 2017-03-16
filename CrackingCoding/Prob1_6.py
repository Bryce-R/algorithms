# Rotate a n*n matrix (clockwise)
def rotate(m,k1,k2):
	n = k2 - k1
	if n == 0:
		return m
	elif n == 1:
		m[k1][k2], m[k2][k2], m[k2][k1], m[k1][k1] = m[k1][k1], m[k1][k2], m[k2][k2], m[k2][k1]
	elif k2-k1 > 1:
		m[k1][k2], m[k2][k2], m[k2][k1], m[k1][k1] = m[k1][k1], m[k1][k2], m[k2][k2], m[k2][k1]
		for i in range(k1+1,k2):
			j = k1+k2-i
			m[i][k2], m[k2][j], m[j][k1], m[k1][i] = m[k1][i], m[i][k2], m[k2][j], m[j][k1]
		rotate(m,k1+1,k2-1)


n = 10
m = [[i+j for i in range(n)] for j in range(0,n*n,n)]
for row in m:
	print row

rotate(m,0,n-1)
print 'Rotate matrix 90 degree clockwise:'
for row in m:
	print row