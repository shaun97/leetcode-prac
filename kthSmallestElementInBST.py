# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # returns the k - number of elements in this subtree
        # returns the kth element
        def dfs(root, kRemaining):
            if root.left != None:
                kRemaining = dfs(root.left, kRemaining)
                if kRemaining[0] < 0:
                    return kRemaining

            # curr node is the kth smallest
            if kRemaining[0] == 1:
                return [-1, root.val]

            kRemaining[0] -= 1

            if root.right != None:
                kRemaining = dfs(root.right, kRemaining)

            return kRemaining

        return dfs(root, [k, -1])[1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()
        stack.append(root)
        visited = set()
        res = root
        while k > 0:
            while stack:
                node = stack.pop()
                if node not in visited:
                    if node.right:
                        stack.append(node.right)
                    stack.append(node)
                    if node.left:
                        stack.append(node.left)
                    visited.add(node)
                else:
                     k -= 1
                     res = node
                     break
        return res.val
