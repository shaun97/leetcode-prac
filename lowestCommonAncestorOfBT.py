# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.res = TreeNode()

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = root
        self.dfs(root, p, q)
        return self.res

    def dfs(self, node, p, q):
        isPFound = False
        isQFound = False

        if node == p:
            isPFound = True
        if node == q:
            isQFound = True

        if node.left:
            temp = self.dfs(node.left, p, q)
            isPFound = temp[0] or isPFound
            isQFound = temp[1] or isQFound

        if node.right:
            temp = self.dfs(node.right, p, q)
            isPFound = temp[0] or isPFound
            isQFound = temp[1] or isQFound

        if isPFound and isQFound:
            self.res = node
            return (False, False)

        return (isPFound, isQFound)

    def lowestCommonAncestorClean(self, root, p, q):
        if root is None:
            return None

        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)

        if (left_res and right_res) or (root in [p, q]):
            return root
        else:
            return left_res or right_res
