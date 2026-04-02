class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        if len(nums) == 2:
            return nums[0]
      
        s=0
        f=len(nums)-1


        while nums[s] != nums[f]:

            if s==f-1:
                s+=1
                f=len(nums)-1
            f-=1

        return nums[s]
            
            
            


        







        



        


        