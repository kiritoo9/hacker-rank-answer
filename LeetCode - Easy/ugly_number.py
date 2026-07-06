class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False

        valid_prime = [2,3,5]
        divisor = 2
        while n > 1:
            if n % divisor == 0:
                n //= divisor
            else:
                divisor += 1
                if divisor > valid_prime[-1]:
                    return False
                
        return divisor in valid_prime