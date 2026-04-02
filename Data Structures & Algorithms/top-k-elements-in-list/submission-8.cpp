class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        

    vector<vector<int>> freq(nums.size() + 1);
    unordered_map<int,int> values;


    for(const auto& n : nums){

        values[n]= 1 + values[n];

    }


    for(const auto& pair : values){

        freq[pair.second].push_back(pair.first);
    }

    vector<int> res;
    for(int i = freq.size() - 1 ; i>=0 ; --i){

        for(int num : freq[i]){

            res.push_back(num);


             if(res.size() == k){

            return res;

        }

        


        }

       

    }
    

return res;

    }
};