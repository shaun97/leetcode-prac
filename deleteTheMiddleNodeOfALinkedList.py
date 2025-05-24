class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=None, next=head)
        fast, slow = head, head
        prev = dummy

        while fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next

            if fast.next:
                fast = fast.next
            else:
                break

        prev.next = slow.next

        return dummy.next
