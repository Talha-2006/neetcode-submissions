class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            diffrence = target - nums[i]

            if diffrence in hashMap:
                return [hashMap[diffrence], i]
            else:
                hashMap[nums[i]] = i