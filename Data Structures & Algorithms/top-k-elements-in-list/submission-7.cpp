class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> bucket(nums.size() + 1);
        unordered_map<int,int> count;


        for (int num : nums) {
            count[num]++;
        }


        for (auto it : count) {
            bucket[it.second].push_back(it.first);
        }
        
        vector<int> res;

        for (int i = bucket.size() - 1; i >= 0; i--) {
            for (int num : bucket[i]) {
                if (k > 0) {
                    res.push_back(num);
                    k--;
                }
                  if (k == 0) break; 
            }
           
        }

        return res;
    }
};