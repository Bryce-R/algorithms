def LCS_length(X,Y):
    m = len(X)
    n = len(Y)
    b = [ [0 for i in xrange(n)] for j in xrange(m) ]
    c = [ [0 for i in xrange(n+1)] for j in xrange(m+1) ]
    for i in xrange(1,m+1):
        for j in xrange(1,n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1]+1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    return c

def print_LCS(X,Y,i,j,c):
    if i==0 or j==0:
        return False
    if X[i-1] == Y[j-1]:
        print X[i-1],
        i -= 1
        j -= 1
    elif c[i-1][j] == c[i][j]:
        i -= 1
    else:
        j -= 1
    print_LCS(X,Y,i,j,c)

X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']
print X
print Y
c = LCS_length(X,Y)
for item in c:
    print item
print 'Sequence reversed:'
print_LCS(X,Y,len(X),len(Y),c)
