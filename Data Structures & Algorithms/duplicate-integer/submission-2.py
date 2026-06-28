class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set(nums)

        return len(nums) != len(hashSet)
         