class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        
        for n in strs:
            count = [0] * 26  
            
        
            for s in n:
                count[ord(s) - ord('a')] += 1
        
            key = tuple(count)
            
          
            if key in hashMap:
                hashMap[key].append(n)
            else:
                hashMap[key] = [n]
        
        return hashMap.values()