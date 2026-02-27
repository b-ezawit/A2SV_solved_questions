class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1

        max_area = min(height[l],height[r])*(r-l)
        while l<r:
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                if height[l+1] < height[r-1]:
                    r -= 1
                else:
                    l += 1
            curr_area = min(height[l],height[r])*(r-l)
            max_area = max(max_area , curr_area)
            
        return max_area


