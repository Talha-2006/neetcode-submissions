class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = defaultdict(list)

        seen = set()

        n = len(grid)
        m = len(grid[0])

        def dfs(cord, parent):
            if cord in seen:
                return
            i = cord[0]
            j = cord[1]

            if grid[i][j] == "1":
                islands[parent].append(cord)
                seen.add(cord)

                if i + 1 < n:
                    dfs((i + 1, j), parent)
                if i - 1 >= 0:
                    dfs((i -1, j), parent)
                if j - 1 >= 0:
                    dfs((i, j - 1), parent)
                if j + 1 < m:
                    dfs((i, j + 1), parent)
            else:
                return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = (i,j)

                if grid[i][j] == "1" and (i,j) not in seen:
                    dfs((i,j), (i,j))
                else:
                    continue
        
        return len(islands)


        