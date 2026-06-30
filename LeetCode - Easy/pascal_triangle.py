class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []

        for i in range(1, numRows+1):
            if i <= 2:
                output.append([1 for _ in range(i)])
            else:
                x = [output[0][0]]
                for j,v in enumerate(output[-1]):
                    if j+1 < len(output[-1]):
                        x.append(v + output[-1][j+1])

                x.append(output[0][0])
                output.append(x)

        return output