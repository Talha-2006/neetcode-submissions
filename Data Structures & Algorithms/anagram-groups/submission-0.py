class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for word in strs:
            if tuple(sorted(word)) in hashMap:
                hashMap[tuple(sorted(word)) ].append(word)
            else: 
                hashMap[tuple(sorted(word)) ] = [word]
        
        return list(hashMap.values())