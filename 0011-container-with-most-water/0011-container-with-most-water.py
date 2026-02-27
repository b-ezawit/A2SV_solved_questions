class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l , r = 0,len(height)-1
        area = maxarea = min(height[l],height[r]) * r-l
        
        while l<r:
            
            if height[l]>height[r]:
                r -= 1
            elif height[l]<height[r]:
                l+=1
            else:
                if height[l+1] > height[r-1]:
                    l += 1
                else:
                    r -= 1
            area = min(height[l], height[r])*(r-l)
            maxarea = max(area,maxarea)
        return maxarea