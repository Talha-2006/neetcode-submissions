class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        def append(x,y, distance):
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return
            if grid[x][y] != 2147483647:
                return
            grid[x][y] = distance
            q.append((x,y))
            return
        
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))

        distance = 1

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                if grid[x][y] == -1:
                    continue
                
                append(x + 1, y, distance)
                append(x - 1, y, distance)
                append(x, y + 1, distance)
                append(x, y - 1, distance)
            
            distance += 1
        
        return

