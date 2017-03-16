# quick sort
def quicksort(l,s,e):
    n = e - s + 1
    if n == 2:
        if l[s] > l[e]:
            l[s], l[e] = l[e], l[s]
        print ' '.join(map(str, l))
    elif n>2:
        pivot = l[e]
        i,j = s,e-1
        while l[i] <= pivot: i += 1
        while l[j] > pivot:  j -= 1
        #print i,j,s,e
        while i<j:
            l[i],l[j] = l[j],l[i]
            while l[i] <= pivot:  i += 1
            while l[j] >  pivot:  j -= 1
        l[j+1],l[e] = l[e], l[j+1]
        #print s,j
        print ' '.join(map(str, l))
        quicksort(l, s, j)
        quicksort(l, j+2, e)
        
def quicksort2(l,s,e):
    n = e - s + 1
    if n == 2:
        if l[s] > l[e]:
            l[s], l[e] = l[e], l[s]
        print ' '.join(map(str, l))
    elif n>2:
        pivot = l[e]
        i,j = s,e-1
        while i<j:
            while l[i] <= pivot and i < e: i += 1
            while l[j] > pivot:  j -= 1
            if i<j:
                l[i],l[j] = l[j],l[i]
            else:
                break
        l[j+1],l[e] = l[e], l[j+1]
        #print s,j
        print ' '.join(map(str, l))
        quicksort2(l, s, j)
        quicksort2(l, j+2, e)
        

            
l = [0, 12, 3, 4, 56, 67, 34, 23, 78, 22, 57, 13, 567, 453, 123]
l1 = [0, 12, 3, 4, 56, 67, 34, 23, 78, 22, 57, 13, 567, 453, 123]
n = len(l)
print 'quicksort'
quicksort(l,0,n-1)
print 'quicksort2'
quicksort2(l1,0,n-1)