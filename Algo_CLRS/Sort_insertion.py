import time

def insertion_sort(l):
    n = len(l)
    for i in range(1, n):
        while i>0 and l[i] < l[i-1]:
            swap = l[i]
            l[i] = l[i-1]
            l[i-1] = swap
            i -= 1
            

#l = [8, 9, 20, 45, 34]   
#l = [8, 9, 20, 45, 34, 28, 92, 112, 6, 19, 25]
l = [8, 9, 20, 45, 34, 28, 92, 112, 6, 19, 25, 67, 900, 892, 1,54,3,6,1,0]

print l
n = len(l)
start = time.time()
insertion_sort(l)
end = time.time()
print l
print end-start
