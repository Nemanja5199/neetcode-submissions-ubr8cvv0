class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
 
        case1 = self.rob_linear(nums[:-1])
        
    
        case2 = self.rob_linear(nums[1:])
        
        return max(case1, case2)
    
    def rob_linear(self, nums: List[int]) -> int:
      
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        mem = [0] * len(nums)
        mem[0] = nums[0]
        mem[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            mem[i] = max(mem[i-1], mem[i-2] + nums[i])
        
        return mem[len(nums) - 1]