class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}

        s = 0
        res = 0

        for num in nums:
            s += num
            diff = s - k

            if diff in hashmap:
                res += hashmap[diff]
            
            if s in hashmap:
                hashmap[s] += 1
            else:
                hashmap[s] = 1
            
        return res