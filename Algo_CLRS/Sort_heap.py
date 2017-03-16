import time
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

       

'''
def swap(l):
    swap = l[0]
    l[0] = l[1]
    l[1] = swap
'''
    
#l = [8, 9, 20, 45, 34]   
#l = [8, 9, 20, 45, 34, 28, 92, 112, 6, 19, 25]
l2 = [8, 9, 20, 45, 34, 28, 92, 112, 6, 19, 25, 67, 900, 892, 1,54,3,6,1,0]



#l2 = [8, 9, 20, 45, 34]  
print 'Heap Sort:'
print l2
start = time.time()
heap_sort(l2)
print l2
end = time.time()
t_heap = end - start
