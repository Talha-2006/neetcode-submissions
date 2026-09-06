class Solution:
    def findMin(self, nums: List[int]) -> int:

        def binary(nums, lowest):
            if len(nums) == 1:
                return min(lowest, nums[0])
            elif len(nums) == 0:
                return lowest
            else:
                mid = (len(nums) // 2) - 1
                if lowest > nums[mid]:
                    lowest = nums[mid]
                    return binary(nums[:mid], lowest)
                else:
                    return binary(nums[mid+1:], lowest)
        
        return binary(nums[1:], nums[0])



        