import time

def cut_rod(p,n):
    m = len(p)
    if n == 0:
        return 0
    q = float("-inf")
    for i in range(1,min(m,n)+1):
        q = max(q, p[i-1]+ cut_rod(p,n-i) )
    return q

def memoized_cut_rod(p,n):
    r = [float("-inf") for i in range(n+1)]
    return memoized_cut_rod_aux(p,n,r)
    
def memoized_cut_rod_aux(p,n,r):
    m = len(p)
    if r[n]>=0: return r[n]
    if n == 0: 
        q = 0
    else: 
        q = float('-inf')
        for i in range(1, min(m,n)+1):
            q = max(q, p[i-1] + memoized_cut_rod_aux(p,n-i,r))
    r[n] = q
    return q

def bottom_up_cut_rod(p,n):
    m = len(p)
    r = [float("-inf") for i in range(n+1)]
    r[0] = 0
    for j in range(1,n+1):
        q = float("-inf")
        for i in range(1,min(m,j)+1):
            q = max(q, p[i-1] + r[j-i] )
        r[j] = q
    return r[n]

def extended_bottom_up_cut_rod(p,n):
    m = len(p)
    r = [float("-inf") for i in range(n+1)]
    s = [-1 for i in range(n+1) ]
    r[0] = 0
    for j in range(1,n+1):
        q = float("-inf")
        for i in range(1,min(m,j)+1):
            if q < p[i-1] + r[j-i]:
                q = p[i-1] + r[j-i]
                s[j] = i
        r[j] = q
    return (r,s)    

p = [1,5,8,9,10,17,17,20,24,30]
n  = 10
print 'Naive Recursion'
start = time.time()
print cut_rod(p,n)
end = time.time()
t1 = start -end
print 'Time: %f' % t1

print 'DP Recursion'
start = time.time()
print memoized_cut_rod(p,n)
end = time.time()
t2 = start -end
print 'Time: %f' % t2

print 'Bottom up'
start = time.time()
print bottom_up_cut_rod(p,n)
end = time.time()
t3 = start -end
print 'Time: %f' % t3

print extended_bottom_up_cut_rod(p,n)
(r,s) = extended_bottom_up_cut_rod(p,n)
while n > 0:
    print s[n]
    n -= s[n]
