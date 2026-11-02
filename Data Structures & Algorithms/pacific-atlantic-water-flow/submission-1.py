class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        #Pacific DFS
        pacific = set()

        stack = [(0, i) for i in range(len(heights[0]))]
        for i in range(len(heights)):
            stack.append((i, 0))
        
        def add(x, y, height):
            if x < 0 or x >= rows or y < 0 or y >= cols or height > heights[x][y]:
                return
            if (x,y) not in pacific:
                stack.append((x,y))

        while stack:
            x, y = stack.pop()
            value = heights[x][y]

            if (x,y) not in pacific:
                pacific.add((x,y))

            add(x + 1, y, value)
            add(x - 1, y, value) 
            add(x, y + 1, value) 
            add(x, y - 1, value)
        
        #Atlantic DFS
        atlantic = set()

        stack = [(rows - 1, i) for i in range(len(heights[rows-1]))]
        for i in range(len(heights)):
            stack.append((i, cols-1))
        
        def add(x, y, height):
            if x < 0 or x >= rows or y < 0 or y >= cols or height > heights[x][y]:
                return
            if (x,y) not in atlantic:
                stack.append((x,y))

        while stack:
            x, y = stack.pop()
            value = heights[x][y]

            if (x,y) not in atlantic:
                atlantic.add((x,y))

            add(x + 1, y, value)
            add(x - 1, y, value) 
            add(x, y + 1, value) 
            add(x, y - 1, value)
        
        res = []

        for cord in pacific:
            if cord in atlantic:
                res.append(list(cord))
        
        return res
        



       


        


        