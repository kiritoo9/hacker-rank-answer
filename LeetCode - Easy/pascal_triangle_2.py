class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        x = [1]
        if rowIndex >= 1:
            x = [1,1]

        output = [x]
        for i in range(2, rowIndex+1):
            x = [1]
            for j,v in enumerate(output[-1]):
                if j+1 < len(output[-1]):
                    x.append(v + output[-1][j+1])
            x.append(1)
            output.append(x)

        return output[-1]