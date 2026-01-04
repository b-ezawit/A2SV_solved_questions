class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currsum = maxsum = nums[0]

        for i in range(1,len(nums)):
            currsum = max(nums[i], currsum+nums[i])
            maxsum = max(currsum,maxsum)
        
        return maxsum
    