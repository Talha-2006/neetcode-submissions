class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_hash = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)

            anagrams_hash[str(sorted_word)].append(word)
        
        res = list(anagrams_hash.values())

        return res

        

        