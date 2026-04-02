class Solution {
public:
    int maxArea(vector<int>& heights) {

    
    int max = 0;



    int l = 0;
    int r = heights.size() -1;


    while ( l < r){

        int sum = 0;
        if( heights[l] >= heights[r]){

        sum = heights[r] * (r-l);
        r--;

        }

        else if( heights[l] <= heights[r]){
            sum = heights[l] * (r-l);
            l++;

        }


        if( sum > max) max = sum;

    }


    return max;

        
    }
};
