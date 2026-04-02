class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:



        hashSet = set(nums)


        longest = 0
        for num in nums:
            count = 1
            while num - 1 in hashSet:
                num-=1
            
            while num + 1 in hashSet:
                num += 1
                count += 1

            longest = max(longest,count) 
        

        return longest


















        
        