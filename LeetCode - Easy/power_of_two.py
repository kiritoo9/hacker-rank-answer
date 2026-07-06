class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        count = 0
        for _ in range(1, 31):
            count = 2 if count == 0 else count*2
            if count == n:
                return True

        return False