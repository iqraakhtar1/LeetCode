# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        root = res = ListNode(None)
        for l in lists:
            while l:
                heappush(heap, l.val)
                l = l.next
        while heap:
            res.next = ListNode(heappop(heap))
            res = res.next
        return root.next