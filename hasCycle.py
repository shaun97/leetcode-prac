class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return False
        first = head
        second = head
        isSecondMove = False

        while first.next != None:
            first = first.next
            if isSecondMove:
                second = second.next
                isSecondMove = False
            else:
                isSecondMove = True

            if first == second:
                return True

        return False

    def hasCycleCleaner(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
