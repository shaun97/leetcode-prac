# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recursiveBuild(numsRemaining):
            length = len(numsRemaining) - 1

            if length == 0:
                return TreeNode(val=numsRemaining[0])
            elif length == -1:
                return None

            mid = length // 2
            leftChild = recursiveBuild(numsRemaining[:mid])
            rightChild = recursiveBuild(numsRemaining[mid + 1:])
            node = TreeNode(
                val=numsRemaining[mid], left=leftChild, right=rightChild)
            return node

        return recursiveBuild(nums)
