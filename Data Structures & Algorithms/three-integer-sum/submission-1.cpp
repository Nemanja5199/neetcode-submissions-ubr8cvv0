class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        sort(nums.begin(), nums.end());

       

        vector<vector<int>> res;
        set<vector<int>> check;
        for(int i = 0 ; i < nums.size() - 1 ; i++){

        
        int l = i + 1;

        int r = nums.size() -1 ;


        while( l < r){


        if(nums[i] + nums[l] + nums[r] == 0){

            if(check.find({nums[i] , nums[l] , nums[r]}) == check.end()){
                check.insert({nums[i] , nums[l] , nums[r]});
                res.push_back({nums[i] , nums[l] , nums[r]});
            }

            l++;
        }

        else if(nums[i] + nums[l] + nums[r] > 0) {

            r--;

        }



        else if(nums[i] + nums[l] + nums[r] < 0) {

            l++;

        }
        

        }
        

        }


        return res;
        
    }
};
