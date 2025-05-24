# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        q = deque()
        q.append(root)
        while len(q) != 0:
            node = q.popleft()
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp

        return root
