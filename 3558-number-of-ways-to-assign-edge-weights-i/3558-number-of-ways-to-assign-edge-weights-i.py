class Solution:
    '''
    Total Ways = (Number of Choices per individual)^(Number of Individuals)
    '''
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph  = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

    
        def dfs(node, parent, currDepth):
            maxD = currDepth

            for nei in graph[node]:
                if nei != parent:
                    maxD = max(maxD, dfs(nei,node,currDepth + 1))
            return maxD
        
        maxDepth =  dfs(1,None,0)
        MOD = (10**9)+7

        return (2 ** (maxDepth - 1)) % MOD
    
    