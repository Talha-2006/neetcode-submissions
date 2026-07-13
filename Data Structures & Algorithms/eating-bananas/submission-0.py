class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k: int):
            count = 0
            for num in piles:
                count += math.ceil(num / k)
            return count

        max_k = max(piles)
        length = len(piles)
        min_k = max_k 

        l, r = 1, max_k 

        while l <= r:
            mid = l + ((r - l) // 2)
            curr_hours = hours(mid)

            if curr_hours <= h:
                min_k = min(min_k, mid)

                r = mid - 1
            else:
                l = mid + 1
        
        return min_k 

        