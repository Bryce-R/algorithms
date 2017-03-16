def answer(h, q):
    # your code here
    def post_traversal(h,k,add):
        root = 2**h-1
        if k == 2**h-2 + add:
            return root + add
        elif k == 2**(h-1)-1 + add:
            return root + add
        elif k < 2**(h-1) + add:
            return post_traversal(h-1,k,add)
        else:
            add += 2**(h-1)-1
            return post_traversal(h-1,k,add)

    n = 2**h -1
    p = [None for i in xrange(len(q))]
    for i in xrange(len(q)):
        if q[i] == n:
            p[i] = -1
        else:
            p[i] =  post_traversal(h,q[i],0)
    return p


h = 3
q = [7,3,5,1]
#q = [5]
print answer(h,q)
