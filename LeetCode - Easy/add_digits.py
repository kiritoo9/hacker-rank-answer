class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def extract(val):
            arr = []
            while val >= 1:
                arr.append(val % 10)
                val //= 10
                
            return sum(arr)
                
        while num >= 10:
            num = extract(num)

        return num