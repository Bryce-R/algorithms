import time
import random
# -----------Quick Sort
def quick_sort(l,b,e):
    if b < e:
        pivot = l[e]
        i = b-1 
        j = b
        while j < e:
            if l[j] < l[e]:
                i += 1
                swap(l, i, j) 
            j += 1
        swap(l, i+1, e)
        quick_sort(l, b, i)
        quick_sort(l, i+2, e)            
       
    
def swap(l,i,j):
    swap = l[i]
    l[i] = l[j]
    l[j] = swap        



    
#l = [8, 9, 20, 45, 34]   
#l = [8, 9, 20, 45, 34, 28, 92, 112, 6, 19, 25]
#l3 = [8, 9, 20, 45, 34, 28, 92, 112, 6, 19, 25, 67, 900, 892, 1,54,3,1,0]



#l3 = [8, 9, 20, 45, 34]  
l3 = range(500, 0, -2)
random.shuffle(l3)
print 'Quick Sort, Before sorting:'
print l3
start = time.time()
quick_sort(l3, 0, len(l3)-1)
end = time.time()
print 'Quick Sort, After sorting:'
print l3

t_quick = end - start
print 'Quick Sort time:'
print t_quick
