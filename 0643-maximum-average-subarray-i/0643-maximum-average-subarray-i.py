class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        curr_sum = sum(nums[:k])
        max_av = float(curr_sum)/k
        for i in range(k,n):
            curr_sum -= nums[i-k]
            curr_sum += nums[i]
            max_av = max(max_av , float(curr_sum)/k)
        return max_av
            
        