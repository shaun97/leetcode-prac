# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p, q))

        while queue:
            pNode, qNode = queue.popleft()

            if pNode == None and qNode == None:
                continue

            if (pNode == None) or (qNode == None) or pNode.val != qNode.val:
                return False

            queue.append((pNode.left, qNode.left))
            queue.append((pNode.right, qNode.right))

        return True
