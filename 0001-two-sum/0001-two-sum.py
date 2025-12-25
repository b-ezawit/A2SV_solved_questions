class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l =0
        r = 1
        res =[]
        while l<len(nums):
            if r ==len(nums):
                l += 1
                r = l+1
                continue

            if nums[l] +nums[r]==target:
                res.append(l)
                res.append(r)
                return res
            else:
                r += 1
    