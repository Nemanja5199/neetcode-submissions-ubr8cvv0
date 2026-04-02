class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        setNums= set()

        for s in nums:
            if s in setNums:
                return True
            else:
                setNums.add(s)
        return False