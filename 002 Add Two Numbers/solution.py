"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # ---------------- Solution 0 -----------  68 ms
        # 1. x = 0 true, others false
        # 2. x = None false
        # 3. code will run in both python2 and python3 use function divmod 
        dummy_head = ListNode(-1)
        current_position = dummy_head
        carry = 0
        while l1 or l2 or carry:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            carry, new_value = divmod(l1_value + l2_value + carry, 10)
            current_position.next = ListNode(new_value)
            current_position = current_position.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next

        # ---------------- Solution 1 -----------  104 ms
        # only can run in python2
        def list_to_num(list):
            num = 0
            count = 0
            while list:
                num = num  + list.val * (10 ** count)
                count += 1
                list = list.next
            return num
        
        return map(int, str(list_to_num(l1) + list_to_num(l2))[::-1])