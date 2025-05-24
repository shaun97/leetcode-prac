# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = dummy
        if not head:
            return

        while curr:
            if curr.next and curr.next.next:
                odd = curr.next
                even = curr.next.next

                odd.next = even.next
                even.next = odd
                curr.next = even

                curr = curr.next
                curr = curr.next
            else:
                break
        return dummy.next
