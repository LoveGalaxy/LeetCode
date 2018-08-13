"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # ---------------- Solution 0 ----------- 
        head = ListNode(-1)
        t = head
        while l1 or l2:
            if not l1:
                t.next = l2
                l2 = None
            elif not l2:
                t.next = l1
                l1 = None
            elif l1.val > l2.val:
                t.next = ListNode(l2.val)
                t = t.next
                l2 = l2.next
            else:
                t.next = ListNode(l1.val)
                t = t.next
                l1 = l1.next
        return head.next