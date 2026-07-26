class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        matrix = []
        for _ in range(numRows):
            matrix.append([])
        
        
        str_count = 0
        y = 0
        to_down = True
        
        while str_count < len(s):
            if to_down:
                matrix[y].append(s[str_count])
                
                if y+1 >= numRows:
                    y -= 1
                    to_down = False
                else:
                    y += 1
            else:
                for j in range((numRows-1), -1, -1):
                    matrix[j].append(
                        s[str_count] if y == j else ""
                    )
                    
                if y-1 < 0:
                    to_down = True
                    y += 1
                else:
                    y -=1
                
            str_count += 1
            
        s = ""
        for i in matrix:
            s += "".join(j for j in i)
            
        return s