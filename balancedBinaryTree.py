# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Recursively expore the tree using DFS, at each node, we compare the height of the left and right child
        return self.isBalancedRecurse(root)[0]

    def isBalancedRecurse(self, root):
        isRBalanced, isLBalanced = (True, 0), (True, 0)
        if root == None:
            return (True, 0)

        if root.right != None:
            isRBalanced = self.isBalancedRecurse(root.right)

        if root.left != None:
            isLBalanced = self.isBalancedRecurse(root.left)

        # we return whether it is balanced and the height of the tree starting from that
        if not isRBalanced[0] or not isLBalanced[0] or (abs(isRBalanced[1] - isLBalanced[1]) > 1):
            return (False, max(isRBalanced[1], isLBalanced[1]) + 1)
        else:
            return (True, max(isRBalanced[1], isLBalanced[1]) + 1)
