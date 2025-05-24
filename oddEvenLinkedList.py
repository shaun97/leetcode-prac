# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head
        dummyOdd, dummyEven = ListNode(), ListNode()
        currOdd, currEven = dummyOdd, dummyEven
        if not head:
            return

        while currNode:
            currOdd.next = currNode
            currOdd = currOdd.next
            currNode = currNode.next

            if currNode:
                currEven.next = currNode
                currEven = currEven.next
                currNode = currNode.next
        if dummyEven.next:
            currOdd.next = dummyEven.next
            currEven.next = None
        else:
            currOdd.next = None
        return dummyOdd.next
