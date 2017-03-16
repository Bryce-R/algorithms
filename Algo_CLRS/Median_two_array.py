def Median_two(a,b,n1,n2):
    al = 0
    ar = n1-1
    bl = 0
    br = n2-1
    while ar-al>1 and br-bl>1:
        if (ar-al)%2 == 0:
            m1 = (a[(ar+al)/2] + a[(ar+al)/2+1])/2
        else:
            m1 = a[(ar+al)/2]
        if (br-bl)%2 == 0:
            m2 = (b[(br+bl)/2] + b[(br+bl)/2+1])/2
        else:
            m2 = b[(br+bl)/2]
        if m1 == m2:
            return m1
        elif m1 < m2:
            al = (ar+al)/2
            br = (br+bl)/2
        else:
            ar = (ar+al)/2
            bl = (br+bl)/2
    print al,ar,bl,br
    return float( ( max(a[al], b[bl]) + min(a[ar], b[br]) )/2)


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        if n%2 == 0:
            return ( float (self.findkth(nums1, nums2, n1, n2, n/2-1)) + float( self.findkth(nums1, nums2, n1, n2, n/2)) )/2
        else:
            return self.findkth(nums1, nums2, n1, n2, n/2)

    def findkth(self, nums1, nums2, n1, n2, k):
        #print k
        if n1 < n2:
            return self.findkth(nums2, nums1, n2, n1, k)
        if n1 == 0:
            return nums2[k]
        elif n2 == 0:
            return nums1[k]
        elif k == 0:
            return min(nums1[0], nums2[0])
        elif n1 == 1:
            if k == 0:
                return min(nums1[0],nums2[0])
            else:
                return max(nums1[0],nums2[0])
        elif n2 == 1:
            if nums1[k-1] >= nums2[0]:
                return nums1[k-1]
            else:
                return min(nums2[0], nums1[k])




        k1 = n1/2
        k2 = max(min(k- k1, n2-1),0)
        print k,k1,k2
        if nums1[k1] >= nums2[k2] and nums2[k2] >= nums1[k1-1]:
            return nums2[k2]
        elif nums1[k1] < nums2[k2] and (nums1[k1] >= nums2[k2-1] or k2 ==0):
            return nums1[k1]
        elif nums1[k1] < nums2[k2]:
            return self.findkth(nums1[k1+1:], nums2, n1-(k1+1), n2, k-(k1+1))
        elif nums1[k1] >= nums2[k2]:
            return self.findkth(nums1, nums2[k2+1:], n1, n2-(k2+1), k-(k2+1))





l = [([1, 12, 15, 26, 38],[2, 13, 17, 30, 45]), ([1,3,5], [2,4]), ([2,7],[1,3,9] ), ([2, 7, 15],[1,3,9] ), ([1,3], [2]), ([3,3,3,3], [3,3,3,3]), ([1],[2,3,4,5,6]), ([100001],[100000]),
([1,4,5,6], [2,3,7,8]) ]
#print Median_two(a,b,len(a),len(b))
s = Solution()
for a,b in l:
    print 'The medians of the two sorted array is:'
    print a,b
    print s.findMedianSortedArrays(a,b)
