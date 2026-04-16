class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        set<int> s(nums.begin(), nums.end());

        int res = 0;

        for (int num : s) {

            
            if (!s.count(num - 1)) {

                int current = num;
                int len = 1;

                while (s.count(current + 1)) {
                    current++;
                    len++;
                }

                res = max(res, len);
            }
        }

        return res;
    }
};