# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        cur = head
        pre = dummy
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = cur
            else:
                pre.next = cur.next
            cur= cur.next
        return dummy.next