class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def max_frequency(counts):
            max_freq = 0
            for char in counts:
                max_freq = max(max_freq, counts[char])
            return max_freq
        
        l = 0
        counts = defaultdict(int)
        length = 0

        max_length = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            max_freq = max_frequency(counts)
            length += 1
    
            if length - max_freq <= k:
                max_length = max(length, max_length)
                continue
                
            else:
                while length - max_freq > k:
                    counts[s[l]] -= 1
                    length -= 1
                    l += 1
                    max_freq = max_frequency(counts)
                max_length = max(length, max_length)
        max_length = max(length, max_length)
        return max_length

        