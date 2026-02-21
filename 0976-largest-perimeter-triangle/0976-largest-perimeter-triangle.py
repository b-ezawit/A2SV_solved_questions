class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if i < 2:
                break
            a = nums[i]
            b = nums[i-1]
            c = nums[i-2]
            if b+c > a:
                return a+b+c
        return 0
