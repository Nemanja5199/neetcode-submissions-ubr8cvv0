class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}


        for i in range(len(s)):

            count[s[i]]= 1 + count.get(s[i],0)

        for i in range(len(s)):

            count[t[i]] = count.get(t[i],0) -1 
        
        return all(count == 0 for count in count.values())

       

      

   

        
       