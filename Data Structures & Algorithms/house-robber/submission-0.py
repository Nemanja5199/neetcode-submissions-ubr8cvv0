class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        mem = [0] * len(nums) 

        mem[0] = nums[0]
        mem[1] = max(nums[0], nums[1])

        for n in range(1 , len(nums)):
            mem[n] = max(mem[n-1], mem[n-2] + nums[n])
        
        return mem[len(nums) - 1]









        