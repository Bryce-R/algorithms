# 8.3 power set of a set


class Solution(object):
	# Recursive solution, slow
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return nums
        elif n == 1:
            return [nums, []]
        else:
            for i in xrange(n):
                l = [nums[j] for j in xrange(n) if j != i]
                exc = self.subsets( l )
            return (exc + [ [nums[i]] + item  for item in exc ] )
    def subsets2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return nums
        else:
            l = [[], [ nums[0] ] ]
            for i in xrange(1,n):
                m = len(l)
                for j in xrange(m):
                    l.append(l[j]+ [nums[i]]) 
            return l
    def subsets3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return nums
        else:
            l = [[], [ nums[0] ] ]
            m = 2
            for i in xrange(1,n):
                li = [[nums[i]]+l[j] for j in xrange(m)]
                m *= 2
                l.extend(li) 
            return l
s = Solution()
l = [1,2,3,4,5,6,7,8,9,10]
#print s.subsets(l)
print s.subsets2(l)
print s.subsets3(l)
