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

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in [None, p, q]: return root
        else:
            (left, right) = (self.lowestCommonAncestor(kid, p , q) for kid in (root.left, root.right))
            if left and right:
                return root
            elif left:
                return left
            else:
                return right

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



s = Solution()
print 'Lowest Common Ancestor:'
anc = s.lowestCommonAncestor(root, root.right.right, root.right.left)
print anc.data
