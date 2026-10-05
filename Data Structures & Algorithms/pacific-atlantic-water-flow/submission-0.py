class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def check_p(r,c, level):
            if (r<0 or c < 0 
            or r >= rows or c >= cols
            or (r,c) in pacific):
                return
            else:
                new_level = heights[r][c]
                if new_level >= level:
                    stack.append((r,c))
                return


        rows, cols = len(heights), len(heights[0])
        pacific = set()

        stack = [(0, c) for c in range(cols)]

        for i in range(rows):
            stack.append((i, 0))
        
        while stack:
            curr = stack.pop()

            if curr not in pacific:
                pacific.add(curr)

                check_p(curr[0] + 1, curr[1], heights[curr[0]][curr[1]])
                check_p(curr[0] - 1, curr[1], heights[curr[0]][curr[1]])
                check_p(curr[0], curr[1] + 1, heights[curr[0]][curr[1]])
                check_p(curr[0], curr[1] - 1, heights[curr[0]][curr[1]])
        


        def check_a(r,c, level):
            if (r<0 or c < 0 
            or r >= rows or c >= cols
            or (r,c) in atlantic):
                return
            else:
                new_level = heights[r][c]
                if new_level >= level:
                    stack.append((r,c))
                return


        rows, cols = len(heights), len(heights[0])
        atlantic = set()

        stack = [(rows - 1, c) for c in range(cols)]

        for i in range(rows):
            stack.append((i, cols - 1))
        
        while stack:
            curr = stack.pop()

            if curr not in atlantic:
                atlantic.add(curr)

                check_a(curr[0] + 1, curr[1], heights[curr[0]][curr[1]])
                check_a(curr[0] - 1, curr[1], heights[curr[0]][curr[1]])
                check_a(curr[0], curr[1] + 1, heights[curr[0]][curr[1]])
                check_a(curr[0], curr[1] - 1, heights[curr[0]][curr[1]])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res


        


        