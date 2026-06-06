class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
      
        rightSum = sum(nums)
        leftSum = 0
        ans = []
        for i in range(len(nums)):
            rightSum -= nums[i]
            ans.append(abs(rightSum - leftSum))
            leftSum += nums[i]
        
        return ans