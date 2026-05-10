class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.minUnfair = float('inf')
        
        bucket = [0]*k
        #[10,20]
        #    j

        #[8,15,10,20,8]
        # 0  1  2  3 4 5 
        #          indx  
        def backtrack(indx,path):
            if indx >= len(cookies):
                self.minUnfair = min(max(path), self.minUnfair)#33
                return

            if max(path) > self.minUnfair:
                return 

            
            for j in range(k):
                path[j] += cookies[indx]
                backtrack(indx+1,path)
                path[j] -= cookies[indx]
            
        
        backtrack(0,bucket)
        return self.minUnfair
