class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        l=1
        r= max(piles) 

        while l<= r:

            mid = l + (r-l) //2

            hours = self.hoursCalculation(mid,piles)

            if hours > h:
                l = mid + 1
            elif hours <= h:
                r = mid - 1
        
        return l
    
    def hoursCalculation(self, k: int, piles: List[int]) -> int:
        hours = 0
        for num in piles:

            hours += (num + k - 1) // k

        return hours  