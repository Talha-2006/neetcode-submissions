class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()

        def dfs(node, parent):
            if node in seen:
                return False

            seen.add(node)

            for child in graph[node]:
                if child == parent:
                    continue

                if not dfs(child, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(seen) == n