class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(start: int, end: int) -> int:
            if start >= end:
                return -1

            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return binary(start, mid)
            else:
                return binary(mid + 1, end)
        
        return binary(0, len(nums))
        