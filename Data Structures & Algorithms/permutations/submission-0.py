class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        res = []

        current_nums = nums.copy()


        def dfs(subset,current_nums):
            print(f"Subset: {subset} , Cur: {current_nums}")

            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in current_nums:
                subset.append(i)
                currnums_copy = current_nums.copy()
                currnums_copy.remove(i)
                dfs(subset, currnums_copy)
                subset.pop()
 
        

        dfs([],current_nums)

        return res
            
            


            

            

            






        