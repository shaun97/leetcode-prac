# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = {}
        count = 0

        def preorder(node, curr_sum):
            nonlocal count
            if not node:
                return

            curr_sum += node.val

            # situation one
            if curr_sum == targetSum:
                count += 1
            if (curr_sum - targetSum) in counter:
                count += counter[curr_sum - targetSum]

            if curr_sum in counter:
                counter[curr_sum] += 1
            else:
                counter[curr_sum] = 1

            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            counter[curr_sum] -= 1

        preorder(root, 0)
        return count
