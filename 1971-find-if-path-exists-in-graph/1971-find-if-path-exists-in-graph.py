class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        
        def dfs(node,visited):
            if node == destination:
                return True
            
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    found = dfs(nei,visited)

                    if found:
                        return True
            return False
        
        return dfs(source,visited)
                