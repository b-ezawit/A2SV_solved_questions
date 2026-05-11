class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0
        hmap = {
            0:"a",
            1:"b",
            2:"c"
        }
        
        def backtrack(indx,path):
            nonlocal count
            if len(path) == n:
                count += 1
                if count == k:
                    return "".join(path)
                return
            

            for j in range(3):
                char = hmap[j]
                if not path or path[-1] != char:
                    path.append(char)
                    
                    res = backtrack(j+1,path)
                    if res:
                        return res

                    path.pop()
        
        if k > 3 * (2**(n-1)):
            return ""  
        
        return backtrack(0,[])
                
        
        