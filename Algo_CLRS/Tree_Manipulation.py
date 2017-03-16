#!/usr/bin/env python -tt

class Node(object):
	def __init__(self, data=None, left_node=None, right_node=None):
		self.data = data
		self.left = left_node
		self.right = right_node

def preOrder(root):
	print root.data,
	if root.left is not None:
		preOrder(root.left)
	if root.right is not None:
		preOrder(root.right)
		
def postOrder(root):
	if root.left is not None:
		postOrder(root.left)
	if root.right is not None:
		postOrder(root.right)
	print root.data,

def inOrder(root):
	if root.left is not None:
		inOrder(root.left)
	print root.data,
	if root.right is not None:
		inOrder(root.right)
	
def T_insert(root, n):
    if root.left is None and n < root.data:
        root.left = Node(n, None, None)
    elif root.right is None and n > root.data:
        root.right = Node(n, None, None)
    elif n < root.data:
        T_insert(root.left, n)
    elif n > root.data:
        T_insert(root.right, n)

def levelOrder(root):
    q = []
    Curr = root
    while Curr is not None:
        print Curr.data,
        if Curr.left is not None:
            q.append(Curr.left)
        if Curr.right is not None:
            q.append(Curr.right)
        if q:
            Curr = q.pop(0)
        else: Curr = None

def graphic_tree(root):
    q1 = [root]
    q2 = []
    while q1 or q2:
        print '\n'
        while q1:
            Curr = q1.pop(0)
            print Curr.data,
            if Curr.left is not None:
                q2.append(Curr.left)
            if Curr.right is not None:
                q2.append(Curr.right)   
        print '\n'    
        while q2:
            Curr = q2.pop(0)
            print Curr.data,
            if Curr.left is not None:
                q1.append(Curr.left)
            if Curr.right is not None:
                q1.append(Curr.right)   

def vertical_order(root):
    d = {}
    lo = 0
    hi = 0
    q = []
    Curr = root
    order = 0
    while Curr is not None:
        lo = min(lo, order)
        hi = max(hi, order)  
        
        if order not in d:
            d[order] = [Curr.data]
        elif order in d:
            d[order].append(Curr.data)
            
        if Curr.left is not None:
            q.append( (Curr.left, order-1) )
        if Curr.right is not None:
            q.append( (Curr.right, order+1) )
            
        if q:
            Curr, order = q.pop(0) 
        else: Curr = None
    for i in range(lo,hi+1):
        print ' '.join(map(str, d[i]))
           
def top_view(root):
    d = {}
    lo = 0
    hi = 0
    q = []
    Curr = root
    order = 0
    while Curr is not None:
        lo = min(lo, order)
        hi = max(hi, order)  
        
        if order not in d:
            d[order] = [Curr.data]
        elif order in d:
            d[order].append(Curr.data)
            
        if Curr.left is not None:
            q.append( (Curr.left, order-1) )
        if Curr.right is not None:
            q.append( (Curr.right, order+1) )
            
        if q:
            Curr, order = q.pop(0) 
        else: Curr = None
    for i in range(lo,hi+1):
        print d[i][0]
                            
'''
l = [3, 7, 8, 6, 4, 1]
#l = [1, 3, 7, 8, 6, 4]
T = Node(5, None, None)
for e in l:
    T_insert(T, e)
'''

# 2nd way to make a tree
T = Node(1, None, None)
T.left = Node(2, None, None)
T.right = Node(3, None, None)
T.left.right = Node(4, None, None)
T.left.right.right = Node(5, None, None)
T.left.right.right.right = Node(6, None, None)



print ' Pre Order Traversal:'
preOrder(T)

print '\n Post Order Traversal:'
postOrder(T)

print '\n In Order Traversal:'
inOrder(T)

print '\n Level Order Traversal:'
levelOrder(T)

print '\n Vertical Order Traversal:'
vertical_order(T)

print '\n Graphical Level Representation'
graphic_tree(T)

print '\nTop view:'
top_view(T)



