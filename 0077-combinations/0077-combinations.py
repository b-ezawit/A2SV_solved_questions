class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1,n+1)]
        ans = []
        def backtrack(i,path):
            if len(path) == k:
                ans.append(path[:])
                return
            
            if i >= n:
                return 
            

            #insert:
            path.append(nums[i])
            backtrack(i+1,path)

            #no insert:
            path.pop()
            backtrack(i+1,path)
        
        backtrack(0,[])
        return ans
        

        


    

            
