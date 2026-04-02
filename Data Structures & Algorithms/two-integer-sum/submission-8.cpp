class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        map<int,int> res;

        for(int i= 0 ; i< nums.size() ; ++i){
            int sum = target - nums[i];

            if(res.count(sum)){
                return {res[sum],i};
            }

            res[nums[i]]=i;
        }   
       return {0,0};
    }
};
