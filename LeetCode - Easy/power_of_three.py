class Solution(object):
    def isPowerOfThree(self, n):
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
            count = 3 if count == 0 else count*3
            if count == n:
                return True
        return False