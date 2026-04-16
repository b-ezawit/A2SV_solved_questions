class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i+1:
                if nums[i] == nums[nums[i]-1]:
                    return nums[i]
                pos = nums[i] - 1
                nums[i],nums[pos] = nums[pos],nums[i]
        
        
        l,r = 0,1
        while r<len(nums):
            if nums[l] == nums[r]:
                return nums[l]
            else:
                l += 1
                r += 1
        