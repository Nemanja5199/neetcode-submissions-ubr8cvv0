class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> myStack;
        
        for(const auto& c : tokens) {
            if(c == "+" || c == "-" || c == "*" || c == "/") {
              
                if(myStack.size() >= 2) {
                    int b = myStack.top();
                    myStack.pop();
                    int a = myStack.top(); 
                    myStack.pop();
                    
                    if(c == "+") {
                        myStack.push(a + b);
                    } else if(c == "-") {
                        myStack.push(a - b);
                    } else if(c == "*") {
                        myStack.push(a * b);
                    } else if(c == "/") {
                        myStack.push(a / b);
                    }
                }
            } else {
              
                myStack.push(stoi(c));
            }
        }
        
        return myStack.top();
    }
};