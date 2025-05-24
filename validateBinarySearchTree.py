# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTRecurse(root)[0]

    def isValidBSTRecurse(self, node):
        # returns a tuple (valid BST, max value, minval) of the tree starting from this node

        maxVal = node.val
        minVal = node.val
        isValid = True

        if node.left:
            leftChild = self.isValidBSTRecurse(node.left)

            if leftChild[1] >= node.val:
                isValid = False

            minVal = min(minVal, leftChild[2])
            isValid = isValid and leftChild[0]

        if node.right:
            rightChild = self.isValidBSTRecurse(node.right)

            if rightChild[2] <= node.val:
                isValid = False
            maxVal = max(maxVal, rightChild[1])
            isValid = isValid and rightChild[0]

        return (isValid, maxVal, minVal)
