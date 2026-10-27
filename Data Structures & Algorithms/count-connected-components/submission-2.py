class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        seen = set()

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            seen.add(node)

            for child in graph[node]:
                if child not in seen:
                    dfs(child)
        
        count = 0
        for node in range(n):
            if node not in seen:
                count += 1
                dfs(node)
        
        return count
        
            

                


        