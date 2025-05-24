# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # returns(maxOfTree, ongoing)
        def max_gain(node):
            if not node.left and not node.right:
                return (node.val, node.val)

            maxOfTree = -math.inf
            ongoing = -math.inf

            leftMaxOfTree, leftOngoing = -math.inf, -math.inf
            rightMaxOfTree, rightOngoing = -math.inf, -math.inf

            if node.left:
                leftMaxOfTree, leftOngoing = max_gain(node.left)

            if node.right:
                rightMaxOfTree, rightOngoing = max_gain(node.right)

            ongoing = max(leftOngoing + node.val,
                          rightOngoing + node.val, node.val)

            maxOfTree = max(leftMaxOfTree, rightMaxOfTree,
                            leftOngoing + rightOngoing + node.val, ongoing)

            return (maxOfTree, ongoing)

        return max_gain(root)[0]
