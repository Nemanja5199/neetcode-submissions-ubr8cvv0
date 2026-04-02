class Solution {
public:
    float getTime(int target, int p, int v) {
        return (float)(target - p) / v;
    }
    
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> pairs(position.size());

        for(int i = 0; i < position.size(); i++) {
            pairs[i] = {position[i], speed[i]};
        } 

        // Sort in descending order by position
        sort(pairs.begin(), pairs.end(), [](const auto& a, const auto& b) {
            return a.first > b.first;
        });

        stack<pair<int, int>> myStack;

        for(const auto& p : pairs) {
            if(myStack.empty()) {
                myStack.push(p);
                continue;
            }

            pair<int, int> top = myStack.top();
            
            
            if(getTime(target, p.first, p.second) <= getTime(target, top.first, top.second)) {
              
            } else {
               
                myStack.push(p);
            }
        }

        return myStack.size();
    }
};