class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        l, r = 0, 1

        res = 0
        curr_len = 1
        
        seen = set()
        seen.add(s[l])

        while r <= len(s) - 1:
            if s[r] in seen:
                res = max(curr_len, res)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                    curr_len -= 1
            else:
                seen.add(s[r])
                curr_len += 1
                r += 1
        res = max(curr_len, res)
        return res
                


        