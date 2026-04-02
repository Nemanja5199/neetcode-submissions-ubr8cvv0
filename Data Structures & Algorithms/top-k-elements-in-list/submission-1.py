class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashset= {}

        for n in nums:
            hashset[n]= 1 + hashset.get(n, 0)
        sorted_list = sorted(hashset.items(), key=lambda item: item[1], reverse=True)

        top_k_values = [item[0] for item in sorted_list[:k]]
            
        return top_k_values

        