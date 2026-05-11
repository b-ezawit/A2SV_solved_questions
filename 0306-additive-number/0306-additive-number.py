class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ans = [] 

        def backtrack(indx):
            if indx == len(num):
                return len(ans) >= 3

            for j in range(indx, len(num)):
                path = num[indx : j + 1] 
                
                if len(path) > 1 and path[0] == '0':
                    break
                
                curr_val = int(path)
                
                if len(ans) >= 2:
                    expected = ans[-1] + ans[-2]
                    if curr_val < expected:
                        continue
                    if curr_val > expected:
                        break
                
                ans.append(curr_val)
                if backtrack(j + 1):
                    return True
                ans.pop()
                
            return False

        return backtrack(0)