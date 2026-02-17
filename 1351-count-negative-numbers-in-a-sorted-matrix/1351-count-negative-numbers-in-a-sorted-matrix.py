class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        total = 0

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if grid[i][j] < 0:
                    total += 1
                else:
                    break
        
        return total

