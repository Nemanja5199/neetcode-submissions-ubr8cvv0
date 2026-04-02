# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        currentNode,previusNode= head,None


        while currentNode:
            temp = currentNode.next
            currentNode.next = previusNode
            previusNode= currentNode 
            currentNode= temp
        return previusNode


        




            
        
        






            
            


        