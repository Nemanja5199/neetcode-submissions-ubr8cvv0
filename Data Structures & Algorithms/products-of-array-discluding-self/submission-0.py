class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product=1
        zero_counter=nums.count(0)

        if zero_counter>1:
            return [0]*len(nums)


        for num in nums:
            if num !=0:
                product*=num
        
        res = []
        if zero_counter == 1:
           
            for num in nums:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
            return res
        
        else:
            for num in nums:
                res.append(product // num)
            return res
        
        
        
        
            

        
           


        



        