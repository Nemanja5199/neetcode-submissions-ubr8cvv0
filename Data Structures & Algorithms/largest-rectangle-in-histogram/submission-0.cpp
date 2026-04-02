class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {

        int max = heights[0];
        for(int i=0 ; i < heights.size() ; i++){

            int min = heights[i];
            int width = 1;
            for(int j = i ; j< heights.size() ; j++){

                if(heights[j] < min){

                    min = heights[j];
                }

                int area = min * width++;

                cout<<area<<'|';
                if(area > max){
                    max = area;
                }

            }


        }


        return max;
        
    }
};
