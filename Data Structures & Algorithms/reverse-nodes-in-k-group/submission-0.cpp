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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head;
        
   
        ListNode* check = head;
        int nodeCount = 0;
        while (check && nodeCount < k) {
            check = check->next;
            nodeCount++;
        }
        
       
        if (nodeCount < k) return head;

        int counter = 1;
        ListNode* curr = head;
        
     
        while(counter < k && curr) {
            curr = curr->next;
            counter++;
        }
        
   
        ListNode* secondPart = curr->next;
      
        curr->next = nullptr;
        
        
        ListNode* reversedFirst = reversList(head);
        
        
        ListNode* reversedSecond = nullptr;
        if (secondPart) {
            reversedSecond = reverseKGroup(secondPart, k);
        }
        
        
        head->next = reversedSecond;
        
        return reversedFirst;
    }

    ListNode* reversList(ListNode* head) {
        ListNode* curr = head;
        ListNode* prev = nullptr;

        while(curr) {
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        
        return prev; 
    }
};