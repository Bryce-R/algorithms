def answer(l):
    # your code here
    def divisible(n,m,memo):
    	if n not in memo:
    		memo[n] = []
    	if m in memo[n]:
    		return True
    	elif n%m == 0:
    		memo[n].append(m)
    		memo[n].append(n/m)
    		return True
    	return False

    n = len(l)
    ct = 0
    memo = {}
    for i in xrange(n):
    	for j in xrange(i+1,n):
    		if divisible(l[j],l[i],memo):
    			for k in xrange(j+1,n):
    				if divisible(l[k],l[j],memo):
    					ct+=1

    return ct

def answer1(l):
    # your code here
    n = len(l)
    ct = 0
    for i in xrange(n):
    	for j in xrange(i+1,n):
    		if l[j]%l[i]==0:
    			for k in xrange(j+1,n):
    				if l[k]%l[j]==0:
    					ct+=1

    return ct

def answer2(l):
    # your code here
    n = len(l)
    ct = 0
    memo = {}
    # for j in xrange(1,n):
    # 	memo[j] = []
    i = 0
    for j in xrange(i+1,n):
    	if l[j]%l[i]==0:
    		memo[j] = []
    	for k in xrange(j+1,n):
    		if l[k]%l[j]==0:
    			memo[j].append(k)
    			ct+= 1

    for i in xrange(1,n):
		for j in memo[i]:
			ct += len(memo[j])


    return ct


l = [[1,1,1],[1,2,3,4,5,6]]
l = [list(range(1,2000))];

for ls in l:
	#print ls
	print answer2(ls)