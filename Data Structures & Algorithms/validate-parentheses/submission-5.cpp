class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> brackets = {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'} 
        };
        
        stack<char> myStack;
        
        for(const auto& p : s) {
            if(brackets.find(p) != brackets.end()) {
                myStack.push(p);
            }
            else {
                if(myStack.empty()) return false;
                
                if(p == brackets[myStack.top()]) {
                    myStack.pop();
                }
                else {
                    return false;
                }
            }
        }
        
      
        return myStack.empty();
    }
};