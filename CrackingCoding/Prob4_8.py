# 4.8 print all paths that sum up to a value
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
                

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None: return []
        if root.left == None and root.right == None:
            if root.data == sum: 
                return [[root.data]]
            else:
                return []
        else:
            if root.data == sum: 
            	middle = [[]]
            else: middle = []
            left, right = (self.pathSum(kid, sum - root.data) for kid in (root.left, root.right) )
            return [[root.data] + i for i in (left + right + middle)]

	def allpath(self, root, sum):
		if root is None:
			return []
		else:
			return self.pathSum(root, sum) + self.allpath(root.left, sum) + self.allpath(root.right, sum)


l = [10,5,-3,3,2,0,11,3,-2,0,1]
l = [10,5,-3,3,-3,0,11,3,-2,0,-1]
sum = -3
print l
root = BinaryTree(l,0,len(l))
graphic_tree(root)
print ''
Inorder(root)
print ''
s = Solution()
print 'Path on a tree'
print s.pathSum(root,sum)
