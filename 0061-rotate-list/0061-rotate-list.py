# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length,cur = 1, head
        while cur.next:
            cur = cur.next
            length+=1
        k = k%length
        node = length -k
        cur.next = head
        last = None
        counter = 1
        dummy = head
        while counter<=node:
            last = dummy
            dummy = dummy.next
            counter+=1
        head= dummy
        last.next= None
        return head
        
        
        
    
            
            
            
        
        
        
        