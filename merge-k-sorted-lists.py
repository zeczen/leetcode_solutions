# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        q = []  # min heap
        out = ListNode(val=-1)
        pos = out
        
        for i in range(k):
            if lists[i]:
                heappush(q, (lists[i].val, i))
                lists[i] = lists[i].next

        while q:
      	    element, i = heappop(q)
            
            pos.next = ListNode(element)
            pos = pos.next
    
            if lists[i]:
                heappush(q, (lists[i].val, i))
                lists[i] = lists[i].next
                
        return out.next
        
