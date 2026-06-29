class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]

#prefix [1, 2, 8, 48]
#postfix [48, 48, 24, 6]

        prefix = []
        curr_product = 1

        for num in nums:
            curr_product *= num
            prefix.append(curr_product)
        
        postfix = [0] * len(nums)
        curr_product = 1

        for i in range(len(nums) - 1, 0, -1):
            curr_product *= nums[i]
            postfix[i] = curr_product

        res = [0] * len(nums)

        for i in range(len(nums)):
            pre_index = prefix[i-1] if i > 0 else 1
            post_index = postfix[i+1] if i < len(nums) - 1 else 1

            res[i] = pre_index * post_index

        return res

