class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def make_hash(hash_map, s):
            for char in s:
                hash_map[char] += 1
        
        l, r = 0, len(s1) - 1
        s1_hash = defaultdict(int)
        s2_hash = defaultdict(int)

        make_hash(s1_hash, s1)
        make_hash(s2_hash, s2[:len(s1)])

        while r <= len(s2) - 2:
            if s1_hash == s2_hash:
                return True
            else:
                s2_hash[s2[l]] -= 1
                if s2_hash[s2[l]] == 0:
                    del s2_hash[s2[l]]
                l += 1
                r += 1
                s2_hash[s2[r]] += 1
        
        if s1_hash == s2_hash:
                return True
        return False

        