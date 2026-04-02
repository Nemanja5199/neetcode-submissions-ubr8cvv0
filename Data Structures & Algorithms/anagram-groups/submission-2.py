class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hashMap= {}


        for s in strs:
            
            sorted_str= ''.join(sorted(s))
            hashMap.setdefault(sorted_str,[]).append(s)
        
        return hashMap.values()
        