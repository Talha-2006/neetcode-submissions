class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)

        while k != 0:
            curr = heapq.heappop(nums)

            k -= 1
        
        return curr * -1
        