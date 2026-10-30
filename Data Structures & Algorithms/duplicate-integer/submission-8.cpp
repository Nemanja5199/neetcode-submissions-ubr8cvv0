class Solution {
public:
    bool hasDuplicate(vector<int>& nums) { 
        set<int> res;


        for(const auto i : nums)
        {
            if(res.count(i))
            return true;

            res.insert(i);
        }

        return false ;
    }
};