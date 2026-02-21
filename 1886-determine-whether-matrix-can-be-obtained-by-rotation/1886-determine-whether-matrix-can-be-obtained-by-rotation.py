class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        rows = len(mat)
        cols = len(mat[0])

        #0 or 360 deg
        if mat == target:
            return True

        #90 deg:
        mat90 = [[0]*rows for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                mat90[c][r] = mat[r][c]

        for row in mat90:
            row[::] = row[::-1]
        
        if mat90 == target:
            return True
        

        #180 deg:
        mat180 = [[0]*rows for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                mat180[c][r] = mat90[r][c]

        for row in mat180:
            row[::] = row[::-1]
        
        if mat180 == target:
            return True
        
        #270 deg:
        mat270 = [[0]*rows for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                mat270[c][r] = mat180[r][c]

        for row in mat270:
            row[::] = row[::-1]
        
        if mat270 == target:
            return True
        
        return False
                
