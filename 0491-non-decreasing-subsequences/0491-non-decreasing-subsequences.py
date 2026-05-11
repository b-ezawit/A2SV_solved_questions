class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(indx,path,length):
            if len(path) == length:
                if path not in ans:
                    ans.append(path[:])
                return
            
            for j in range(indx,len(nums)):
                num = nums[j]
                if not path or path[-1] <= num:
                    path.append(num)
                    backtrack(j+1,path,length)
                    path.pop()

        for l in range(2,len(nums)+1):
            backtrack(0,[],l)

        return ans           

