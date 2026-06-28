class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMapS = {}
        hashMapT = {}

        for charS, charT in zip(s, t):
            if charS in hashMapS:
                hashMapS[charS] += 1
            if charT in hashMapT:
                hashMapT[charT] += 1
            
            if charS not in hashMapS:
                hashMapS[charS] = 1
            if charT not in hashMapT:
                hashMapT[charT] = 1
        
        return hashMapS == hashMapT
            
            
        