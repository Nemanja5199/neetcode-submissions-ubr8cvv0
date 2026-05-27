class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMap = defaultdict(int)

        for c in s:
            hashMap[c]+=1
        for c in t:
            hashMap[c]-=1
        
        for n in hashMap.values():
            if n !=0:
                return False
        return True


        