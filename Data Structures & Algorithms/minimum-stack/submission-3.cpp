class MinStack {
private:
    vector<pair<int, int>> stack; // Each element stores (value, min at this level)
    
public:
    void push(int val) {
        int currentMin = stack.empty() ? val : min(val, stack.back().second);
        stack.push_back({val, currentMin});
    }
    
    void pop() {
        if (!stack.empty()) stack.pop_back();
    }
    
    int top() {
        return stack.back().first;
    }
    
    int getMin() {
        return stack.back().second;
    }
};