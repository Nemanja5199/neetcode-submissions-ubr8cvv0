# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        
       
        newList = ListNode(0)
        head= newList
        carry=0
        while l1 and l2:
            Sum=0
            Sum= l1.val + l2.val + carry
            newNode= ListNode(0)
            if Sum >= 10:
                newNode.val = Sum % 10
                carry= Sum // 10
            else:
                newNode.val = Sum
                carry=0
            newList.next=newNode
            newList=newList.next
                
            l1=l1.next
            l2=l2.next
        
        if l1 :
            while l1:
                Sum=0
                Sum= l1.val  + carry
                newNode= ListNode(0)
                if Sum >= 10:
                    newNode.val = Sum % 10
                    carry= Sum // 10
                else:
                    newNode.val = Sum
                    carry=0
                newList.next=newNode
                newList=newList.next
                l1=l1.next

        elif l2:
            while l2:
                Sum=0
                Sum= l2.val  + carry
                newNode= ListNode(0)
                if Sum >= 10:
                    newNode.val = Sum % 10
                    carry= Sum // 10
                else:
                    newNode.val = Sum
                    carry=0
                newList.next=newNode
                newList=newList.next
                l2=l2.next
        
        if carry> 0:
            newNode = ListNode(carry)
            newList.next=newNode

        return head.next

