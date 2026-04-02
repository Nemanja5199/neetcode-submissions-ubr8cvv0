class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}

        for n in nums:
            hashMap[n]= hashMap.get(n,0) + 1
        

        count = [[] for i in range(len(nums) +1)]

        for num,value in hashMap.items():
            count[value].append(num)
        
        res = []
        for i in range(len(count) - 1 , 0 , -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res
        