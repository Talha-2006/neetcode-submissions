class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        saved = set()
        stack = []
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != "O":
                    continue
                if i == 0 or i == rows-1:
                    stack.append((i,j))
                elif j == 0  or j == cols-1:
                    stack.append((i,j))
        
        def addN(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            else:
                if board[r][c] == "O":
                    stack.append((r,c))
                return

        while stack:
            r,c = stack.pop()
            
            if (r,c) not in saved:
                saved.add((r,c))

                addN(r+1, c)
                addN(r-1, c)
                addN(r, c+1)
                addN(r, c-1)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] != "O":
                    continue
                elif (i,j) in saved:
                    continue
                else:
                    board[i][j] = "X"
                    
