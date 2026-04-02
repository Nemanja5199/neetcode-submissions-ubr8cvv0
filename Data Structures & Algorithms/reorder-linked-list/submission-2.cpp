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

    ListNode* reverse(ListNode* head){

        ListNode* curr = head;
        ListNode* i = nullptr;

        while(curr){
        
            ListNode* temp = curr;
            curr = curr->next;
            temp->next = i;
            i=temp;
        }

        return i;
    }



    void reorderList(ListNode* head) {


        ListNode* slow = head;
        ListNode* fast = head;


        while(fast && fast->next){

            slow = slow->next;
            fast = fast->next->next;

        }
        

        
         ListNode* p2 = slow -> next;
         slow->next= nullptr;
        ListNode* p1= head;

        p2 = reverse(p2);

        ListNode* curr = p1;
        while(p1 && p2){

        p1 = p1->next;
        curr->next = p2;
        curr = p2;
        p2 = p2->next;
        curr->next = p1;
        curr = p1;    
        }



        
        
    }
};
