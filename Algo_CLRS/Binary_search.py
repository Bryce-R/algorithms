import time
import random

def Merge_sort(l,b,e): #b: beginning and e: end.
    if e-b > 2:
        Merge_sort(l, b, b+(e-b)/2)
        Merge_sort(l, b+(e-b)/2, e)
        merge(l, b, e)   
    elif e-b == 2: 
        if l[b] > l[b+1]:
            swap = l[b+1]
            l[b+1] = l[b]
            l[b] = swap 

def merge(l,b,e):
    n = e-b
    l1 = l[b: b+(e-b)/2]
    l2 = l[b+(e-b)/2: e]
    k1 = 0
    k2 = 0
    k = b
    while k1<len(l1) and k2 <len(l2):
        if l1[k1] < l2[k2]:
            l[k] = l1[k1]
            k1 += 1
        else:
            l[k] = l2[k2]
            k2 += 1
        k += 1
    if k2 == len(l2):
        l[k:e] = l1[k1:]
    else:
        l[k:e] = l2[k2:]

def binary_search_recur(l, lo, hi, n):
    #print lo, hi
    if lo == hi and l[lo] == n:
        print (True, lo)
    elif lo == hi or hi < lo:
        print 'Doesn\'t exist.'
    elif lo < hi:
        m = (lo + hi)/2
        if n < l[m]:
            binary_search(l, lo, m-1, n)
        elif n > l[m]:
            binary_search(l, m+1, hi, n)
        else: 
            print (True, m)
        
def binary_search(l, lo, hi, n):
    while lo <= hi:
        m = (lo+hi)/2
        if n == l[m]:
            print m
            break
        elif lo ==hi:
            print False
            break
        elif n < l[m]:
            hi = m-1
        elif n > l[m]:
            lo = m+1
    else:
        print False 
        
def binary_search_v2(l, lo, hi, n):
    while(hi - lo > 1):
        m = (hi+lo)/2
        if n<=l[m]:
            hi = m
        else:
            lo = m+1
    if n == l[lo]:
        print lo
    elif n == l[hi]:
        print hi
    else: 
        print -1         


#l = [8, 9, 20, 45, 34]   
#l = [8, 9, 20, 45, 34, 28, 92, 112, 6, 19, 25]
#l = [8, 9, 20, 45, 34, 28, 92, 112, 6, 19, 25, 67, 900, 892, 1,54,3,6,1,0]
'''
num = 100
l = range(num,0,-2)
random.shuffle(l)
print 'Merge Sort, Before Sorting: '
print l
n = len(l)
#b = 0 #beginning
#e = n #end

start = time.time()
Merge_sort(l,0,n)
end = time.time()
print 'Merge Sort, After Sorting: '
print l
t_merge =  end-start
'''

l = range(0,1000,2)
print l
#binary_search(l, 0, len(l)-1, 23)
print 'Recursion:'
print 'No recursion:'
print 'v2'
t = [5, 23, 34, 56, 67, 198, 142, 173, 155]
for num in t:
    print 'Search for number: %d' % num
    start = time.time()
    binary_search_recur(l, 0, len(l)-1, num)
    end = time.time()
    t_rec = start -end
    start = time.time()
    binary_search(l, 0, len(l)-1, num)
    end = time.time()
    t_1 = start -end
    start = time.time()
    binary_search_v2(l, 0, len(l)-1, num)
    end = time.time()
    t_2 = start - end
    print 'Recursion time: %d' % t_rec
    print 'v1: %d' % t_1
    print 'V2: %d' % t_2


'''
for num in t:
    print 'Search for number: %d' % num
    binary_search(l, 0, len(l)-1, num)
    
'''
