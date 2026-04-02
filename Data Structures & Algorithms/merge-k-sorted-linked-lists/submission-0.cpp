/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
       
        if (lists.empty()) return nullptr;
        
        vector<ListNode*> pointers(lists.size());
        
        for(int i = 0; i < lists.size(); i++) {
            pointers[i] = lists[i];
        }
        
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        
        while(true) {
           
            int nullPointerCount = 0;
            int minIndex = -1;
            
            for(int i = 0; i < pointers.size(); i++) {
                if (pointers[i] == nullptr) {
                    nullPointerCount++;
                } else if (minIndex == -1) {
                   
                    minIndex = i;
                }
            }
            
            
            if (nullPointerCount == pointers.size()) {
                break;
            }
            
            
            for(int i = 0; i < pointers.size(); i++) {
                if (pointers[i] != nullptr && pointers[i]->val < pointers[minIndex]->val) {
                    minIndex = i;
                }
            }
           
            curr->next = pointers[minIndex];
            curr = curr->next;
         
            pointers[minIndex] = pointers[minIndex]->next;
        }
        
        return dummy->next;
    }
};