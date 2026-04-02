class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:



        hashMap = {}
        hashCount = {}
        for i in range(len(nums) + 1):
            hashMap[i] = []
        
        for num in nums:

            hashCount[num] = hashCount.get(num, 0) + 1
        
        for key in hashCount:
            hashMap[hashCount[key]].append(key)

        res = []
        for i in range(len(nums), -1 , -1):

            for num in hashMap[i]:
                if k >0:
                    res.append(num)
                    k-=1
        return res
        
        

        

        


            










   
        