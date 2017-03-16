def edit_dist(X,Y,m,n):
    if m == 0 or n ==0:
        return m+n
    elif X[m-1] == Y[n-1]:
        return edit_dist(X,Y,m-1,n-1)
    else:
        return 1 + min( edit_dist(X,Y,m,n-1), edit_dist(X,Y,m-1,n), edit_dist(X,Y,m-1,n-1) )

def edit_dist_m(X,Y,m,n):
    c = [ [0 for i in xrange(n)] for j in xrange(m) ]

    for i in xrange(n):
        c[0][i] = i
    for j in xrange(m):
        c[j][0] = j
    #print c
    for j in xrange(1,m):
        for i in xrange(1,n):
            #print i, j
            if X[j] == Y[i]:
                c[j][i] = c[j-1][i-1]
            else:
                c[j][i] = 1 + min(c[j][i-1], c[j-1][i], c[j-1][i-1])
    return c[m-1][n-1]


l = [('geek', 'gesek'), ('cat','cut'), ('sunday', 'saturday')]
for X,Y in l:
    m = len(X)
    n = len(Y)
    print 'The edit distance between:',X,'and',Y
    print edit_dist(X,Y,m,n),edit_dist_m(X,Y,m,n)
