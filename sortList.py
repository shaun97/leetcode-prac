# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # takes in the head of the portion that it is supposed to sort
        def mergeSort(mergeHead) -> Optional[ListNode]:

            # if head is none
            if mergeHead == None:
                return

            # if it is single case
            if mergeHead.next == None:
                return mergeHead

            # find the half way point
            dummy = ListNode(next=mergeHead)
            fastPtr, slowPtr = dummy, dummy
            while fastPtr.next:
                fastPtr = fastPtr.next
                slowPtr = slowPtr.next

                if fastPtr.next:
                    fastPtr = fastPtr.next
            prev = slowPtr
            slowPtr = slowPtr.next
            prev.next = None

            firstHalf = mergeSort(dummy.next)
            secondHalf = mergeSort(slowPtr)

            # merge these two lists
            currPtr = dummy
            while firstHalf and secondHalf:
                if firstHalf.val > secondHalf.val:
                    currPtr.next = secondHalf
                    secondHalf = secondHalf.next
                else:
                    currPtr.next = firstHalf
                    firstHalf = firstHalf.next
                currPtr = currPtr.next
            if firstHalf != None:
                currPtr.next = firstHalf
            elif secondHalf != None:
                currPtr.next = secondHalf
            return dummy.next

        res = mergeSort(head)
        return res
