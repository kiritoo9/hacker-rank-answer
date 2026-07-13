# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                if isBadVersion(mid) and isBadVersion(mid-1) is False:
                    return mid
                
                right = mid-1
            else:
                left = mid+1