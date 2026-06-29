class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        counts = list(hashMap.values()) #[1,2,3]

        counts = sorted(counts, reverse=True) #[3,2,1]

        final = []
        i = 0

        while k > 0:
            curr_count = counts[i]
            i += 1
            for num in hashMap:
                if hashMap[num] == curr_count and num not in final:
                    final.append(num)
                    break
            k -= 1
        
        return final
        