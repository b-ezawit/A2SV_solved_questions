class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        #[1,3] n=6
        ops = 0
    
        postfix = 0 
        current = 1
        
        for i in range(len(nums)):
            if postfix >= n:
                return ops

            while nums[i] > postfix+1 and nums[i] != 1: # 34 > 12
                if postfix >= n:
                    return ops
                postfix += current #23
                current = postfix + 1 #
                ops += 1 # 
            postfix += nums[i] # 11
            current = postfix + 1 # 12

        while postfix < n:
            postfix += current
            current = postfix + 1
            ops += 1
            
        return ops

            