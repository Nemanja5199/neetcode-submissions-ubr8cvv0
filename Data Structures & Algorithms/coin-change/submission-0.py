class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        mem = [float('inf')] * (amount + 1)
        mem[0] = 0 
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i: 
                    mem[i] = min(mem[i], mem[i - coin] + 1)
        
        return mem[amount] if mem[amount] != float('inf') else -1