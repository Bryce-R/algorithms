# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 00:13:33 2017

@author: Pengkai
"""

def topo_sort(l):
    d = {}
    l1 = []
    l2 = []
    visited = {}
    for item in l:
        if item[0] not in l1:
            l1.append(item[0])
            visited[item[0]] = 0
        if item[1] not in l:
            l1.append(item[1])
            visited[item[1]] = 0
            
        if item[1] not in d:
            d[item[1]] = [item[0]]
        else:
            d[item[1]].append(item[0])
    #print d
    #print l  
    print l1  
    lc = []    
    for u in l1:
    '''
        if cycle_det(u,d,lc) == True:
            print 'cycle exists'
            return u '''
        if u not in l2:
            dfs_visit(u,d,l2,visited,[])
    
    return l2
'''                
def cycle_det(u,d,lc):
    if u in lc:
        return 
    lc.append(u)
    for v in d[u]:
        cycle_det(v,d,lc)
'''
def dfs_visit(u,d,l2,visited,cycle):
    if u in d:
        for v in d[u]:
            if visited[v] == 0:
                dfs_visit(v,d,l2,visited)
    visited[u] = 1
    l2.append(u)
    #if u not in l2:
        #l2.append(u)

       
#l = [(1,22),(2,23),(22,48),(23,45),(3,48)]
l = [('Mo','Mo Mom'), ('Kelvin', 'Kelvin dad'), ('Kelvin dad', 'Kelvin grandpa'), ('Mo_s son','Mo'), ('Denish', 'Denish dad')]
#l = [('Mo','Mo Mom'), ('Kelvin', 'Kelvin dad'), ('Kelvin dad', 'Kelvin grandpa'), ('Mo_s son','Mo'), ('Denish', 'Denish dad'), ('Kelvin grandpa', 'Kelvin')]
print 'Parent Relations'
print l
l1 = topo_sort(l)
l2 = []
while len(l1) > 0:
    l2.append( l1.pop())
    
print 'Birth Order:'
print l2
