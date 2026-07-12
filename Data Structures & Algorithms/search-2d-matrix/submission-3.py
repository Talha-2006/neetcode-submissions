class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_matrix(start: int, end: int):
            mid = start +(end - start) // 2
            if len(matrix[start:end]) < 1:
                return -1
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid])-1]:
                return mid
            elif len(matrix[start:end]) <= 1:
                return -1
            elif matrix[mid][0] > target:
                return binary_matrix(start, mid)
            else:
                return binary_matrix(mid + 1, end)
        
        def binary(start: int, end: int, lst: List[int]):
            mid = start +(end - start) // 2

            if lst[mid] == target:
                return True
            elif len(lst[start:end]) <= 1:
                return False
            elif lst[mid] > target:
                return binary(start, mid, lst)
            else:
                return binary(mid + 1, end, lst)
        
        index = binary_matrix(0, len(matrix))

        if index == -1:
            return False
        
        return binary(0, len(matrix[index]), matrix[index])

        