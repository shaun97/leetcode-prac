# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        dummy = ListNode(None)
        dummy.next = node
        curr = dummy

        while curr.next:
            print(curr.val)
            prev = curr
            curr = curr.next
            if curr.val == node.val:
                prev.next = curr.next
        return dummy.next
