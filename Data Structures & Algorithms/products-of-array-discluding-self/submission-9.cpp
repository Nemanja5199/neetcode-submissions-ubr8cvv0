class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        vector<int> res(nums.size());

        for ( int i = 0 ; i < nums.size() ; ++i){
            if(i == 0 ){
                res[i] = 1;
                continue;
            }

            res[i] = nums[i - 1 ] * res[i -1];
        }

        int suffix = 1;
        for( int i = nums.size() -1    ; i >= 0 ; --i){
            res[i] *=suffix;
            suffix*=nums[i]; 
        }

        return res;
    }
};
