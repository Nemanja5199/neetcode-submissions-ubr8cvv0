class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashMap;
        
        for(const auto& str : strs) {
            vector<int> count(26, 0);
            
            for(auto & s : str) {
                count[s - 'a']++;
            }
            
            string key = "";
            for(int i = 0; i < 26; i++) {
               
                key += to_string(count[i]) + ",";
            }
            
            hashMap[key].push_back(str);
        }
        
        vector<vector<string>> result;
        for (const auto& pair: hashMap) {
            result.push_back(pair.second);
        }
        
        return result;
    }
};