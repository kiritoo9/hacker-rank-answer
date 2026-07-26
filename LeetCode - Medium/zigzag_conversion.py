class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
    
        matrix = [[] for _ in range(numRows)]
        row = 0
        dir = 0
        
        for char in s:
            matrix[row].append(char)
            
            if row == 0:
                dir = 1
            elif row == numRows - 1:
                dir = -1
                
            row += dir
            
        return "".join("".join(row) for row in matrix)