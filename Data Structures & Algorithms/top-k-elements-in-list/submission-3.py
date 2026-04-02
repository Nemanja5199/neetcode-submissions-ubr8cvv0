class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}


        for n in nums:
            hashMap[n]= hashMap.get(n,0) + 1
        
        sorted_dict = dict(sorted(hashMap.items(), key=lambda x: x[1], reverse=True))

       
        result = list(sorted_dict.keys())[:k]

        return result
        
        






        
        