class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        prefix =[1] * len(nums)

        suffix = [1] * len(nums)

        prefix_product=1
        suffix_product=1

        for i,num in enumerate(nums):

            prefix_product*=num
            prefix[i]=prefix_product 
        
        for i in range(len(nums)-1, -1,-1):

            suffix_product*=nums[i]
            suffix[i]= suffix_product
        
        res =  []
        for i in range(len(nums)):

            if i==0:
                res.append(suffix[i+1])
            elif i== len(nums)-1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1]*suffix[i+1])
        
        return res




        




            



    
        
        
        
            

        
           


        



        