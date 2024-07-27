# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPre, cur = dummy, head
        for i in range(left - 1):
            leftPre, cur = cur, cur.next
            
        pre = None
        for i in range(right - left +1):
            tempNext = cur.next
            cur.next = pre
            pre, cur = cur, tempNext
        
        leftPre.next.next = cur
        leftPre.next = pre
        return dummy.next
        
       