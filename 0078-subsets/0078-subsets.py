class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(indx,path,length):
            if len(path) == length:
                ans.append(path[:])
                return
            
            for j in range(indx,len(nums)):
                path.append(nums[j])
                backtrack(j+1,path,length)
                path.pop()
        

        ans = []
        for l in range(len(nums)+1):
            backtrack(0,[],l)

        return ans
