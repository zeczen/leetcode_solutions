# https://leetcode.com/problems/reverse-nodes-in-k-group
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #return head
        sentinel = ListNode(-1, head)
        l = sentinel
        pos = l

        while True:
            for _ in range(k):
                pos = pos.next
                if not pos: return sentinel.next

            pos = l.next
            for _ in range(k-1):
                # move pos.next after l
                prv = l.next
                tmp = pos.next.next
                l.next = pos.next
                pos.next = tmp
                l.next.next = prv

            l = pos
