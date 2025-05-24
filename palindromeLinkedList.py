# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(val=-1, next=head)
        end, mid = dummy, dummy
        prevNode, nextNode = dummy, dummy
        isOdd = False

        if not head.next:
            return True

        while end.next:
            end = end.next
            # start reversing the mid
            nextNode = mid.next
            mid.next = prevNode
            prevNode = mid
            mid = nextNode
            if end.next:
                end = end.next
            else:
                isOdd = True
                break

        if isOdd:
            nextNode = mid.next
        else:
            nextNode = mid.next
            mid.next = prevNode
            prevNode = mid

        while prevNode.val != -1:
            if prevNode.val != nextNode.val:
                return False
            else:
                prevNode = prevNode.next
                nextNode = nextNode.next

        return True
