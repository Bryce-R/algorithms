#!/usr/bin/env python -tt



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
# 4.5 Successor problem 
# Solution 1
def Inorder_q(root,q,node):
    if root.left is not None:
        Inorder_q(root.left, q, node)
    q.append( (root, root==node))
    if root.right is not None:
        Inorder_q(root.right, q, node) 

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == p:
            return p
        elif root == q:
            return q
        else:
            if self.covers(root.left, p) and self.covers(root.left, q):
                return self.lowestCommonAncestor(root.left, p, q)
            elif self.covers(root.right, p) and self.covers(root.right, q):
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root

    def covers(self, node, A):
        if node is None:
            return False
        elif node == A:
            return True
        else:
            l = self.covers(node.left, A)
            r = self.covers(node.right, A)
            return (l or r)
        
    
        


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
                



    

l = [i for i in xrange(1,7)]

print l
root = BinaryTree(l,0,len(l))
graphic_tree(root)
Inorder(root)

q = [] 
node = root
Inorder_q(root,q,node)
print '\nSuccessor node after node %d:' % node.data
for i in range(len(q)):
    if q[i][1] == True:
        print q[i+1][0].data

s = Solution()
print 'Lowest Common Ancestor:'
anc = s.lowestCommonAncestor(root, root.right.right, root.right.left)
print anc.data







