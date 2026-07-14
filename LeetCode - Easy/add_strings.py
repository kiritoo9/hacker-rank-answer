class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1)-1
        j = len(num2)-1
        c = 0
        o = []
        
        while i >= 0 or j >= 0 or c > 0:
            d1 = int(num1[i]) if i >= 0 else 0
            d2 = int(num2[j]) if j >= 0 else 0
            
            r = (d1+d2)+c
            c = r//10
            o.append(r%10)
            
            i -= 1
            j -= 1
        
        o = list(reversed(o))
        return "".join(str(s) for s in o)