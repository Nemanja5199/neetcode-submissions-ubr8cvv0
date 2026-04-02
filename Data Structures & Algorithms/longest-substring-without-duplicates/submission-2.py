class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:




        l = 0
        r= 0 

        maxCount = 0
        charSet = set()
        for r in range(len(s)):

            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            
            charSet.add(s[r])
            maxCount= max(maxCount, r - l + 1)

           
        return maxCount
              



        


        


        