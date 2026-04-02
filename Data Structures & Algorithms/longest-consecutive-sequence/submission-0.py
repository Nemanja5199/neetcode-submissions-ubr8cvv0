class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        numbers = set(nums);
        longest= 0
        for i,num in enumerate(numbers):

            if num - 1 not in numbers:
                count=0
                while num in numbers:
                    count+=1
                    num+=1
                
                longest= max(longest,count)
        
        return longest
                    


            

            











    
        
            
        







        