class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums= sorted(candidates)
        res = []
      

        def dfs(i,target,curr):
            
            if target < 0 :
                return 

            if target == 0:
                res.append(curr.copy())
                return
            
            for j in range(i,len(nums)):
                if j> i and nums[j] == nums[j-1]:
                    continue
                curr.append(nums[j])
                target -= nums[j]
                dfs(j+1,target,curr)
                target += curr.pop()
        
        dfs(0,target,[])

        return res
        