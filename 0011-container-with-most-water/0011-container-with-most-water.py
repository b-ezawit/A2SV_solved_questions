class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1

        maxA = 0

        while left<right:
            area = (right-left)*min(height[left],height[right])
            maxA = max(maxA,area)

            if height[left]<height[right]:
                left += 1
            elif height[left]>height[right]:
                right -= 1

            else:
                if height[left+1]>height[right-1]:
                    left += 1
                else:
                    right -= 1
                    
        return maxA





        