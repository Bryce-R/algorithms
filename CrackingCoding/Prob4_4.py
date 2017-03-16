#!/usr/bin/env python -tt
class LL_node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head):
    while head is not None:
        print head.val,
        head = head.next
    print ''


class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def Inorder(root):
    if root.left is not None:
        Inorder(root.left)
    print root.data,
    if root.right is not None:
        Inorder(root.right) 

def BinaryTree(l,lo,hi):
    n = hi - lo
    if n == 1:
        root = Node(l[lo])
    elif n > 1:
        if n%2 == 0:
            k = n/2 - 1 + lo
        else: k = n/2 + lo
        root = Node(l[k])
        root.left = BinaryTree(l,lo,k)
        root.right = BinaryTree(l, k+1, hi)
    else: 
        return None
    return root

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
                
# 4.4 Create a linked list of all nodes at each depth
def LL_leveltraversal(root):
    q1,q2 = [root],[]
    LL = [] 
    level = -1
    while q1 or q2:
        if q1:
            level += 1
            LL.append([LL_node(-1)])
            Curr = LL[level][0]
            while q1:
                item = q1.pop(0)
                Curr.next = LL_node(item)
                Curr = Curr.next
                if item.left != None: q2.append(item.left)
                if item.right != None: q2.append(item.right)
        if q2:
            level += 1
            LL.append([LL_node(-1)])
            Curr = LL[level][0]
            while q2:
                item = q2.pop(0)
                Curr.next = LL_node(item)
                Curr = Curr.next
                if item.left != None: q1.append(item.left)
                if item.right != None: q1.append(item.right)
    return LL



    

l = [i for i in xrange(1,7)]

print l
root = BinaryTree(l,0,len(l))
graphic_tree(root)
Inorder(root)
LL = LL_leveltraversal(root)
print '\nLinked list in each level'
for l in LL:
    head = l[0].next
    print ''
    while head is not None:
        print head.val.data,
        head = head.next








