class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:



        

        hashMap = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1


            key = tuple(count)
            hashMap[key].append(s)
        

        return hashMap.values()



            

            



        