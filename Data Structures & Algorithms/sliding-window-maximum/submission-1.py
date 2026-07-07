class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k-1
        max_heap = []
        res = []

        for i in range(k-1):
            heapq.heappush(max_heap, (-nums[i], i))
        
        while r <= len(nums) - 1:
            heapq.heappush(max_heap, (-nums[r], r))

            while max_heap[0][1] < l or max_heap[0][1] > r:
                heapq.heappop(max_heap)
            
            curr_max = -max_heap[0][0]
            res.append(curr_max)

            l += 1
            r += 1
        
        return res

        