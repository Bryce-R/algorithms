#Python program for Bellman-Ford's single source
# shortest path algorithm


edge = [(0,1,-1), (0,2,4), (1,2,3), (1,3,2), (1,4,2), (3,2,5), (3,1,1), (4,3,-3)];
n = 5

print 'Edges and their respetive weights:'
print edge

def bellman_ford(edge,n):
    d = {0:0}
    pre = {}
    for i in xrange(1,n):
        d[i] = float("inf")
        pre[i] = None
    for i in xrange(1,n):
        for (u,v,w) in edge:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                pre[v] = u
    for (u,v,w) in edge:
        if d[v] > d[u] + w:
            print False 
    print "Distance from source: \n",d
    print "Predecessors on shortes path: \n",pre
    
bellman_ford(edge,n)
              
                    
        
