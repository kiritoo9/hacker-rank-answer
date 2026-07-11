# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        left = 0
        right = n
        while left <= right:
            mid = left + (right-left) // 2
            p = guess(mid)
            if p == 0:
                return mid
            elif p == -1:
                right = mid-1
            elif p == 1:
                left = mid+1