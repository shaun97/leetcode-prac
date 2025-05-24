# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        regular_head = head.next
        # split into two halves
        if head.next == None or head.next.next == None:
            return

        reversed_head = head
        end = head.next

        while end:
            end = end.next
            if end:
                end = end.next
            else:
                break
            reversed_head = reversed_head.next

        # break
        end_of_regular = reversed_head
        reversed_head = reversed_head.next
        end_of_regular.next = None

        # reverse the list
        prev = None
        curr = reversed_head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        reversed_head = prev

        # merge these two list
        curr = head
        while regular_head != None or reversed_head != None:
            if reversed_head:
                curr.next = reversed_head
                curr = curr.next
                reversed_head = reversed_head.next

            if regular_head:
                curr.next = regular_head
                curr = curr.next
                regular_head = regular_head.next
                
    def reorderListClean(self, head: ListNode) -> None:
        if not head:
            return 
        
        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next       

        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next