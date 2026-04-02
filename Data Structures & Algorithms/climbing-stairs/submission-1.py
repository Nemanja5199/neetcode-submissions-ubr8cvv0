class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        f1 = 1
        f2 = 2

        for i in range(2,n):
            current = f1 + f2
            f1 = f2
            f2 = current
        
        return f2








 
