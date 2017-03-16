import time
import random
def Merge_sort(l,b,e):
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
######### Insertion Sort
def insertion_sort(l):
    n = len(l)
    for i in range(1, n):
        while i>0 and l[i] < l[i-1]:
            swap = l[i]
            l[i] = l[i-1]
            l[i-1] = swap
            i -= 1
            
# -----------Heap Sort
def heap_sort(l):
    n = len(l)
    for i in range(n/2+1,-1,-1):
        max_heapify(l,i,n)
    for i in range(n-1,0,-1):
        swap = l[i]
        l[i] = l[0]
        l[0] = swap
        max_heapify(l,0,i)   


def max_heapify(l,i,n):
    largest = i 
    left = 2*(i+1)-1
    right = 2*(i+1)
    if left<n and l[left]>l[i]:
        largest = 2*(i+1)-1   
    if right<n and l[right] > l[largest]:
        largest = 2*(i+1)
    if largest != i:
        swap = l[i]
        l[i] = l[largest]      
        l[largest] = swap
        max_heapify(l,largest,n)

# -----------Quick Sort
def quick_sort(l,b,e):
    if b < e:
        #swap(l, e, random.randint(b,e-1))
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
#l = [8, 9, 20, 45, 34, 28, 92, 112, 6, 19, 25, 67, 900, 892, 1,54,3,6,1,0]
num = 100
l = range(num,0,-1)
random.shuffle(l)
print l
n = len(l)
#b = 0 #beginning
#e = n #end
print 'Merge Sort: '
start = time.time()
Merge_sort(l,0,n)
end = time.time()
print l
t_merge =  end-start




#l = [8, 9, 20, 45, 34]   
#l = [8, 9, 20, 45, 34, 28, 92, 112, 6, 19, 25]
#l1 = [8, 9, 20, 45, 34, 28, 92, 112, 6, 19, 25, 67, 900, 892, 1,54,3,6,1,0]
l1 = range(num,0,-1)
print 'Insertion Sort: '
print l1
n = len(l1)
start = time.time()
insertion_sort(l1)
end = time.time()
print l1
t_insertion =  end-start

l2 = range(num,0,-1)
print 'Heap Sort:'
print l2
start = time.time()
heap_sort(l2)
end = time.time()
print l2
t_heap = end - start


l3 = range(num,0,-1)
#l3 = [8, 9, 20, 45, 34, 28, 92, 112, 6, 19, 25]
random.shuffle(l3)
print 'Quick Sort, Before sorting:'
print l3
start = time.time()
quick_sort(l3, 0, len(l3)-1)
end = time.time()
print 'Quick Sort, After sorting:'
print l3
t_quick = end - start



print 'Merge sort time:' 
print t_merge
print 'Insertion Sort time'
print t_insertion
print 'Heap Sort Time'
print t_heap
print 'Quick Sort time:'
print t_quick

