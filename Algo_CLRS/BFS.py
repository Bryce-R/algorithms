# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 23:36:16 2017

@author: Pengkai
Breath First search
"""
g = {}
g[0] = [1,2]
g[1] = [2]
g[2] = [0,3]
g[3] = [3]

print 'Nodes and adjacency lists:'
print g

def BFS(g,s):
    q = [s]
    visited = {s:1}
    d = {s:0}
    pi = {s:None}
    while q:
        u = q.pop(0)
        print u,
        for v in g[u]:
            if v not in visited:
                visited[v] = 1
                d[v] = d[u]+1
                pi[v] = u
                q.append(v)
    return (d,pi)


d, pi = BFS(g,2)
print ''
print 'Distances:'
print d 
print 'Predecessor:'
print pi


                
            
