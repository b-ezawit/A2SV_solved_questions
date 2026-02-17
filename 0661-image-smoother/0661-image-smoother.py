class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
         img = [[100,200,100],
                [200,50,200],
                [100,200,100]]
        '''
        
        rows = len(img)
        cols = len(img[0])
        res = [[0] * cols for _ in range(rows)]


        for r in range(rows):
            for c in range(cols):
                curr_sum = curr_count = 0
                for new_row in range(max(0,r-1) , min(rows,r+2) ):
                    for new_col in range(max(0, c-1), min(cols,c+2)):
                        curr_sum += img[new_row][new_col]
                        curr_count += 1
                res[r][c] = curr_sum //curr_count
        
        return res
        