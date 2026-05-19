class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = {i : i for i in range(n)}

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        def merge(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            par[px] = py
        
        for r in range(n):
            for c in range(r + 1):
                if isConnected[r][c]:
                    merge(r, c)
        count = 0
        for i in range(n):
            if i == find(i):
                count += 1
                
        return count