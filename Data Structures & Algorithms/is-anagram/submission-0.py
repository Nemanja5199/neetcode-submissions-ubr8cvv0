class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmaps = {}
        hashmapt = {}

        for n, j in zip(s, t):
            if n in hashmaps:
                hashmaps[n] += 1
            else:
                hashmaps[n] = 1

            if j in hashmapt:
                hashmapt[j] += 1
            else:
                hashmapt[j] = 1

        return hashmaps == hashmapt
