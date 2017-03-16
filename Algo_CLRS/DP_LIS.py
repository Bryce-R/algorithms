def LIS(X):
    n = len(X)
    L = [1 for i in xrange(n)]
    ml = 1
    mi = -1
    pi = {}
    for i in xrange(1,n):
        for j in xrange(i):
            if X[j] < X[i]:
                L[i] = max(L[i], 1 + L[j])
                pi[i] = j
                if ml < L[i]:
                    ml,mi = L[i],i
    return ml,mi,pi

def print_seq(pi,X,i):
    if i in pi:
        print_seq(pi,X,pi[i])
    print X[i],






X = [20, 9, 12, 45, 18, 34, 27, 89]
print X
l, i, pi = LIS(X)
print 'Longest Length: %d' % l
print 'Last index in seq: %d' % i
print pi
print_seq(pi,X,i)
