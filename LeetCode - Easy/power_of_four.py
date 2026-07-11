class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        elif n == 1:
            return True

        count = 0
        for _ in range(1, 31):
            count = 4 if count == 0 else count*4
            if count == n:
                return True
        return False