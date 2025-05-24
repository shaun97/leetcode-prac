# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        delim = -1
        curr_level = []

        if root == None:
            return []

        q.append(root)
        q.append(delim)

        while q:
            curr = q.popleft()
            if curr == delim:
                q.append(delim)
                curr = q.popleft()
                res.append(curr_level)
                curr_level = []

                if not q:
                    break

            curr_level.append(curr.val)

            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)

        return res
