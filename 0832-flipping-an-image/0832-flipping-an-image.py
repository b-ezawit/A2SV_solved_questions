class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """

        '''
        approach:
          1st: flip horizontally == reverse each row
          2nd: invert it, each 1 to 0 or vice-verse

          [[1,1,0],
           [1,0,1],
           [0,0,0]]
        


        '''
        rows = len(image)
        cols = len(image[0])

        for row in image:
            row[::] = row[::-1]

        for i in range(rows):
            for j in range(cols):
                if image[i][j]:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        return image
