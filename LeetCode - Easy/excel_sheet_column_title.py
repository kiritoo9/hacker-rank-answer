import string

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        alpha = list(string.ascii_uppercase)
        hm = {k:v for k,v in enumerate(alpha)}

        output = []
        while columnNumber > 0:
            columnNumber -= 1
            d = columnNumber % len(alpha)
            output.append(hm[d])
            columnNumber //= len(alpha)
            
        return "".join(s for s in output[::-1])