# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        leftH = 0
        rightH = 0
        node = root
        while node:
            leftH += 1
            node = node.left

        node = root
        while node:
            rightH += 1
            node = node.right

        if leftH == 1:
            return 1
        
        # complete binary tree
        if leftH == rightH:
            return 2**leftH - 1

        res = 2**(leftH - 1) - 1

        q = deque()
        q.append((root, leftH))

        while q:
            node, height = q.pop()
            leftHeight = height
            # print(node.val)
            temp = node.left
            while temp:
                leftHeight -= 1
                temp = temp.right
            
            temp = node.right
            rightHeight = height
            while temp:
                rightHeight -= 1
                temp = temp.left

            if rightHeight - leftHeight  == 1:
                # height = 2
                print(node.val)
                print(height)
                res += 2 ** (height - 2)
            elif leftHeight == 1:
                res += 2 ** (height - 2)
                q.append((node.right, height - 1))
            else:
                q.append((node.left, height - 1))
            
        return res