class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        def backtrack(indx,path,length):
            if indx == length:
                if path not in ans:
                    ans.append(path[:])
                return
            
            for j in range(indx,len(nums)):
                path.append(nums[j])
                backtrack(j+1,path,length)
                path.pop()
            

        for l in range(1,len(nums)+1):
            backtrack(0,[],l)
        return ans

                
                