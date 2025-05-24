# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = []

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        self.dfs(root)

        for node in self.nodes:
            diameter = max(diameter, node[0] + node[1])

        return diameter

    def dfs(self, root):
        if root.left == None and root.right == None:
            return 1

        height_from_leaf = 0
        right_height = 0
        left_height = 0
        if root.left != None:
            left_height = self.dfs(root.left)
            height_from_leaf = max(left_height, height_from_leaf)
        if root.right != None:
            right_height = self.dfs(root.right)
            height_from_leaf = max(right_height, height_from_leaf)

        self.nodes.append((left_height, right_height))
        return height_from_leaf + 1
