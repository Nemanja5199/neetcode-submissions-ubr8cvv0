class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not nums:
            return False

    
        numSet = set()


        for num in nums:
            
            if num in numSet:
                return True
            else:
                numSet.add(num)
        return False



        

   
         