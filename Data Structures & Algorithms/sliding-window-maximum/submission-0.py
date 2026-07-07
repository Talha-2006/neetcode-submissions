class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k-1
        max_heap = []
        res = []
        
        while r <= len(nums) - 1:
            max_heap = nums[l:r+1]
            max_heap =[-x for x in max_heap]
            heapq.heapify(max_heap)
            

            curr_max = -max_heap[0]
            res.append(curr_max)

            l += 1
            r += 1
        
        return res

        