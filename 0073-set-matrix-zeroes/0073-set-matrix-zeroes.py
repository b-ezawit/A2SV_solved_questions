class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat = [row[:] for row in matrix]
        rows = len(matrix)
        cols = len(matrix[0])
        check = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0 :
                    curr_row = i
                    curr_col = j
                    for c in range(cols):
                        matrix[curr_row][c] = 0
                    
                    for r in range(rows):
                        matrix[r][curr_col] = 0
                
                    

        return matrix