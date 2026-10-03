class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
        
        def addFruit(r,c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                grid[r][c] != 1
            ):
                return
            else:
                grid[r][c] = 2
                q.append((r,c))
                visited.add((r,c))

        time = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                addFruit(r + 1, c)
                addFruit(r-1, c)
                addFruit(r, c+1)
                addFruit(r, c-1)
            time += 1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return max(time, 0)

        