class Solution {
public:
    void generateHelper(string current, int left, int right, int n, vector<string>& result) {
        
        if (left == n && right == n) {
            result.push_back(current);
            return;
        }
        
       
        if (left < n) {
            generateHelper(current + '(', left + 1, right, n, result);
        }
        
        
        if (right < left) {
            generateHelper(current + ')', left, right + 1, n, result);
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> result;
        generateHelper("", 0, 0, n, result);
        return result;
    }
};