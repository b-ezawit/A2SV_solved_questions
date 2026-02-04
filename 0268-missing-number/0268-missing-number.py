class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 not in nums:
            return 0
        maxNum = max(nums)
        nums.sort()
        l,r = 0,1
        while r<len(nums):
            if nums[r] - nums[l] > 1:
                return nums[l]+1
            l+=1
            r+=1
        return maxNum + 1