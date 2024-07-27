# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # store values of the nodes in a list
        values = []
        while head:
            values.append(head.val)
            head = head.next

        # calculate twin sums for the first half of the list
        twin_sums = [values[i] + values[-(i + 1)] for i in               range(len(values) // 2)]

        # return the maximum twin sum
        return max(twin_sums)
        