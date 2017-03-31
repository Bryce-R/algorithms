
def answer2(l):
    n = len(l)
    ct = 0
    memo = {}
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
