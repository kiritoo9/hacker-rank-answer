class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for d in digits:
            num = num*10+d
        num += 1

        result = []
        while num > 0:
            result.append(num%10)
            num //= 10

        result.reverse()
        return result

        