class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        sqrt_x = 0

        while left <= right:
            mid = (left + right) // 2
            if mid**2 <= x:
                sqrt_x = mid
                left = mid + 1
            else:
                right = mid - 1
            
        return sqrt_x

        #Space = O(1)
        #Time = O(logn)
      

