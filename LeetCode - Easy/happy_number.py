class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t = n
        dp = set()
        
        while True:
            a = []
            while t > 0:
                a.append(t%10)
                t //= 10
            
            total = sum([i*i for i in a])
            
            if total in dp:
                return False
            elif total == 1:
                return True
            else:
                t = total
                dp.add(total)