class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            row_set = set()
            count = 0
            for num in row:
                if num != '.':
                    count += 1
                    row_set.add(num)
        
            if count != len(row_set):
                return False
        
        
        for i in range(9):
            col_set = set()
            count = 0
            for row in board:
                num = row[i]
                if num != '.':
                    count += 1
                    col_set.add(num)

            if count != len(col_set):
                return False

        for i in range(0, 9, 3):
            row_1 = board[i]
            row_2 = board[i+1]
            row_3 = board[i+2]

            for j in range(0, 9, 3):
                box_set = set()
                count = 0
                
                if row_1[j] != '.':
                    count += 1
                    box_set.add(row_1[j])
                if row_2[j] != '.':
                    count += 1
                    box_set.add(row_2[j])
                if row_3[j] != '.':
                    count += 1
                    box_set.add(row_3[j])
                if row_1[j+1] != '.':
                    count += 1
                    box_set.add(row_1[j+1])
                if row_2[j+1] != '.':
                    count += 1
                    box_set.add(row_2[j+1])
                if row_3[j+1] != '.':
                    count += 1
                    box_set.add(row_3[j+1])
                if row_1[j+2] != '.':
                    count += 1
                    box_set.add(row_1[j+2])
                if row_2[j+2] != '.':
                    count += 1
                    box_set.add(row_2[j+2])
                if row_3[j+2] != '.':
                    count += 1
                    box_set.add(row_3[j+2])

                if count != len(box_set):
                    return False
        
        return True
