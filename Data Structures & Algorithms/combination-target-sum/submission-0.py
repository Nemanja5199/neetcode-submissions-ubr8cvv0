class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        res = []
        curr = []

        def dfs(i,target,curr):
            
            if target < 0 :
                return 

            if target == 0:
                res.append(curr.copy())
                return
            
            for j in range(i,len(nums)):
                curr.append(nums[j])
                target -= nums[j]
                dfs(j,target,curr)
                target += curr.pop()
        
        dfs(0,target,curr)

        return res


            
