class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(indx,path):
            if indx >= len(s):
                for i in range(1,len(path)):
                    if path[i-1] - path[i] != 1:
                        return False
                return len(path) >= 2
            
            for i in range(indx,len(s)):
                #append current val
                path.append(int(s[indx:i+1]))

                #call backtrack at the next
                if backtrack(i+1, path):
                    return True
                
                #if the next path doesnot return True, pop it
                path.pop()


            return False
        
        return backtrack(0,[])
            

                
        

        