# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        s,f = head,head 

        while f.next and f.next.next :
            s= s.next
            f=f.next.next

        l1=s.next
        s.next=None
        
        
        l2=self.reverseList(l1)

    
        
        l1= head
        while l1 and l2:
            temp = l2.next
            l2.next=l1.next
            l1.next=l2
            l1=l2.next
            l2=temp
        
        
        
        
        

        

            
       

        

        





    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None

        while curr:
            temp = curr
            curr= curr.next
            temp.next= prev
            prev = temp
        return prev
    
   


        





       
        


        