class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        freq_list = []

        for num in freq:
            freq_list.append((-1 * freq[num], num))
        
        heapq.heapify(freq_list)
        
        res = []

        while k > 0:
            curr = heapq.heappop(freq_list)

            res.append(curr[1])
            k -= 1
        return res


        