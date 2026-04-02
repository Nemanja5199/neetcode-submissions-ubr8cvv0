class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {


        unordered_map<int,int> r;
   
        for (int i=0 ; i< nums.size() ; i ++){
            r[nums[i]]= i;
        }


         vector<int> arr ;
         

        for (int i=0 ; i< nums.size() ; i++){

            int diff = target- nums[i];

            if(r.count(diff) && r[diff] != i){
          
                return {i , r[diff]};
            }

        }
        
        
    }
};
