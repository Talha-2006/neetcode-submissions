class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        lst = []
        #[0,0,0,0]
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                if curr_sum == 0:
                    temp_lst = [nums[i], nums[l], nums[r]]
                    if temp_lst not in lst:
                        lst.append(temp_lst)
                    l += 1
                    r -= 1

                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1
        
        return lst
        