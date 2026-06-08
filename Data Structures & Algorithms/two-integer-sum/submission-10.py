class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myMap = dict()

        for i,num in enumerate(nums):
            res = target - num
            if res in myMap:
                return [myMap[res],i]
            else:
                myMap[num] = i
        
        return None
        

        