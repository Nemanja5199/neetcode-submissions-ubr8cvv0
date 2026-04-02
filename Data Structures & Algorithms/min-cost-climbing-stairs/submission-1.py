class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        mem = [0] * (len(cost) + 1)


        mem[0] = 0
        mem[1] = 0


        for n in range(2 , len(cost) + 1):
            mem[n] = min(mem[n- 1] + cost[n-1] , mem[n-2] + cost[n-2])
        

        return mem[len(cost)]


        

        