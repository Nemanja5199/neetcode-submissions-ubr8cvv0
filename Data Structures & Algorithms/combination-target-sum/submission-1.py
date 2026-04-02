class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        
        subset = []

        res = [] 


        def dfs(subset,index):

            if sum(subset) > target or index >= len(nums):
                return
            
            if sum(subset) == target:
                res.append(subset.copy())
                return res
            
            subset.append(nums[index])
            dfs(subset,index)
            subset.pop()
            dfs(subset,index + 1)
        

        dfs(subset,0)

        return res



            



        