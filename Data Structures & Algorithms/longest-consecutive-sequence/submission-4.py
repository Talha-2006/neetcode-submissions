class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_num = 0

        for num in nums:
            if num - 1 not in num_set:
                curr_seq = 1
                curr_num = num
                
                while curr_num + 1 in num_set:
                    curr_seq += 1

                    curr_num += 1
                
                max_num = max(max_num, curr_seq)
            else:
                continue
        
        return max_num
        

        