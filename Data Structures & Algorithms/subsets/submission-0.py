class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = [[]]

        for i in range(len(nums)):
            
         result = self.makeSubset(nums,i,result)
        
        return result


    


    def makeSubset(self, nums: List[int], index: int, subset: List[List[int]]) -> List[List[int]]:        
        for i in range(len(subset)):
            
            newSubset= subset[i].copy()
            newSubset.append(nums[index])
            subset.append(newSubset)
        
        return subset
        




        











        