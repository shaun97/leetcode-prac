# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTreeNaive(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        startRoot = TreeNode(preorder[0])

        def recursiveBuild(preorder, inorder):
            if len(preorder) == 0:
                return None
            root = TreeNode(val=preorder[0])
            leftTreeInorder = []
            rightTreeInorder = []
            #pre-order [3,9,10,20,15,7]
            # in-order [10,9,3,15,20,7]

            leftTreePreorder = []
            rightTreePreorder = []
            for idx, i in enumerate(inorder):
                if i == root.val:
                    leftTreeInorder = inorder[:idx]
                    rightTreeInorder = inorder[idx + 1:]

            leftTreePreorder = preorder[1:len(leftTreeInorder) + 1]
            rightTreePreorder = preorder[len(leftTreeInorder) + 1:]

            root.left = recursiveBuild(leftTreePreorder, leftTreeInorder)
            root.right = recursiveBuild(rightTreePreorder, rightTreeInorder)

            return root

        return recursiveBuild(preorder, inorder)

        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def __init__(self):
        self.preOrderIndex = 0
        self.preorder = []
        self.inorder = []
        self.inorderHash = {}

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for index, value in enumerate(inorder):
            self.inorderHash[value] = index

        self.preorder = preorder
        self.inorder = inorder

        return self.arrayToTree(0, len(preorder) - 1)

        # start an end denotes the section of the inorder list we are looking at

    def arrayToTree(self, start, end):
        if start > end:
            return None

        rootVal = self.preorder[self.preOrderIndex]
        root = TreeNode(rootVal)
        self.preOrderIndex += 1

        root.left = self.arrayToTree(start, self.inorderHash[root.val] - 1)
        root.right = self.arrayToTree(self.inorderHash[root.val] + 1, end)

        return root
