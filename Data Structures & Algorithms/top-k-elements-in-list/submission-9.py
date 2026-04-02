class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hashMap = {}

        count = [[] for i in range(len(nums) + 1)]


        for num in nums:
           hashMap[num] = 1 + hashMap.get(num,0) 


        for key,val in hashMap.items():

            count[val].append(key)

    
        res = []


        for i in range(len(count) - 1, -1 , -1):

            for num in count[i]:
                if k == 0:
                    return res
                res.append(num)
                k-=1
        
        return res
            
        






        