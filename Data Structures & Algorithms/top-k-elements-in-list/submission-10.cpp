class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        unordered_map<int,int> elements; 
        vector<vector<int>> freq(nums.size() + 1); 

        for (auto &e : nums) {
            elements[e]++;
        }

        for (const auto &pair : elements) {
            freq[pair.second].push_back(pair.first);
        }

        vector<int> res;

        for (int i = freq.size() - 1; i >= 0; i--) {
            for (int num : freq[i]) {
                res.push_back(num);
                if (res.size() == k) {
                    return res;
                }
            }
        }

        return res; 
    }
};
