from queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Iterate through each list simultaneously
        # Compare the heads of each list, pick the lowest one to add it to the final list
        # Use a p queue of size k for the comparison
        q = PriorityQueue()
        count = 0

        head = None

        for index, l in enumerate(lists):
            if l is not None:
                q.put((l.val, count, l))
                count += 1

        if q.qsize() > 0:
            node = q.get(block=False)[2]
            if node.next is not None:
                q.put((node.next.val, count, node.next))
                count += 1
            head = node
            curr = node

        while q.qsize() > 0:
            node = q.get()[2]
            # Put back a new node from the list that it was taken from
            if node.next is not None:
                q.put((node.next.val, count, node.next))
                count += 1
            curr.next = node
            curr = curr.next

        return head
