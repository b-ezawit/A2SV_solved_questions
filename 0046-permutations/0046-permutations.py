class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(indx,path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for j in range(len(nums)):
                if nums[j] not in path:
                    path.append(nums[j])
                    backtrack(j+1,path)
                    path.pop()
        

        backtrack(0,[])
        return ans

        