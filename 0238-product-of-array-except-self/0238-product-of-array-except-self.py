class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #nums =   [5,2,3,4] 
        '''
        postfix = 24
        output = [24, 60, 40, 30]

        '''
        prefix = postfix = 1
        ans = []
        for i in range(len(nums)):
            ans.append(prefix)
            prefix *= nums[i]
        
        for j in range(len(nums)-1,-1,-1):
            ans[j] *= postfix
            postfix *= nums[j]
        
        return ans
