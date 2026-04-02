class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:



        hashMap = {}


        for i,num in enumerate(nums):

            val = target - num

            if val in hashMap:
                return[hashMap[val] , i]
            
            hashMap[num] = i
        
        return False
        

 

            



        