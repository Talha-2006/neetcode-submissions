class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        max_len = 0
        l = 0
        num_set = set()
        num_set.add(s[l])

        for r in range(1, len(s)):
            if s[r] in num_set:
                max_len = max(max_len, r - l)

                while s[r] in num_set:
                    num_set.remove(s[l])
                    l += 1

                num_set.add(s[r])
            else:
                num_set.add(s[r])

        max_len = max(max_len, len(s) - l)
        return max_len
        
        