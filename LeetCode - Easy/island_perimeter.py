class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        per = 0
        ylen = len(grid)
        xlen = len(grid[0])
        
        # handler
        def _check_top(i, j):
            c = 0
            if i == 0:
                c += 1
            else:
                if grid[i-1][j] == 0:
                    c += 1
            return c
        
        def _check_left(i, j):
            c = 0
            if j == 0:
                c += 1
            else:
                if grid[i][j-1] == 0:
                    c += 1
            return c
        
        def _check_right(i, j):
            c = 0
            if j+1 == xlen:
                c += 1
            else:
                if grid[i][j+1] == 0:
                    c += 1
            return c
        
        def _check_bottom(i, j):
            c = 0
            if i+1 == ylen:
                c += 1
            else:
                if grid[i+1][j] == 0:
                    c += 1
            return c
        
        # executor
        for i in range(ylen):
            for j in range(xlen):
                if grid[i][j] == 1:
                    per += _check_top(i, j)
                    per += _check_left(i, j)
                    per += _check_right(i, j)
                    per += _check_bottom(i, j)

        return per