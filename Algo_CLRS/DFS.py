# -*- coding: utf-8 -*-
"""
Created on Jan 02 2017

@author: Pengkai
Depth First search
"""
g = {}
g[0] = [1,2]
g[1] = [2]
g[2] = [0,3]
g[3] = [3]

print 'Nodes and adjacency lists:'
print g

def DFS(g,s,n):
    for v in range(1,n+1):
        visited[v] = 0
    visited[s] = 1
    d = {s:0}
    for v in g[s]:
        print v
        if visited[v] == 0:
            DFS_visit(g,v)

def DFS_visit(g,v):
    


d, pi = DFS(g,2)
print ''
print 'Distances:'
print d 



                
            
