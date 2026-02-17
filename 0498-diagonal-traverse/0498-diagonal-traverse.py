class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
        '''
        to right = up -> right,   row-1 -> col+1
        to left = left->down,     col-1 -> row+1

        out of bound cases: 
        1. to change from upright to bottom-left, going row-1 and col+1  to change to    col-1 and row+1 : 
           a. col is valid, curr_row < 0 but curr_col is valid(is not > total-cols)  : only do row+1, same column
               -> if row<0 and col<cols, then move to bottom-left, to col-1 and row+1  until, col<0 or row>total-rows
           b. col is not valid, col>total-colums, curr_row < 0  and col>col_total at the right-corner. 
               -> here, row+2 and col-=1 , then go back ttraversing bottom-left, col-1, row+1
        
        2. to change from bottom-left to upright, going from col-1 and row+1
            a. col<0 but row is valid, row<total-rows, so only col+=1
            b. row is not valid: row>total-row , do:  col+=2 and row-=1



        coding approach:
        start from up right:
        while r>0:
            res.append(mat[r][c])
            r -= 1
            c += 1
        if r<0 and c<cols:
            r += 1
        elif r<0 and c>cols:
            r += 2
            c -= 1
        
        while c>0:
            res.append(mat[r][c])
            c -= 1
            r += 1
        
        if c<0 and r<rows:
            c += 1
        elif  r>rows:
            c += 2
            r -= 1           

        '''
        res = []
        rows = len(mat)
        cols = len(mat[0])
        r = c = 0
        go_up = True

        while len(res) != rows * cols:
            if go_up:
                while r>=0 and c<cols:
                    res.append(mat[r][c])
                    r -= 1
                    c += 1
                
                if c<cols:
                    r += 1
                else:
                    r += 2
                    c -= 1
                go_up = False
            
            else:
                while c>=0 and r<rows:
                    res.append(mat[r][c])
                    c -= 1
                    r += 1

                if r<rows:
                    c += 1
                else:
                    c += 2
                    r -= 1
                
                go_up = True
        
        return res




            
           

