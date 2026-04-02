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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
          if (head->next == nullptr && n == 1) {
            delete head;
            return nullptr;
        }
        


     ListNode* s = head;
     ListNode* f =  head;

    int count=0;
     while(count < n && f){
        f= f->next;
        count++;
     } 


    if(f == nullptr){

        ListNode* newhead = head->next;
        delete head;
        return newhead;

    }

     while(f->next){

        s=s->next;
        f= f->next;
     }

     cout<<s->val;
    ListNode* temp = s->next;
    s->next = s->next->next;

    delete temp;

    return head;






        
    }
};
