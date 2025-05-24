# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we use bfs to explore the whole graph and keep taking the right most element.

        delim = TreeNode(val=-1)
        res = []

        prevNode = root

        q = deque()

        if root == None:
            return res

        q.append(root)
        q.append(delim)

        while q:
            curr = q.popleft()
            if curr == delim:
                res.append(prevNode.val)
                prevNode = curr

                if len(q) == 0:
                    break

                q.append(delim)
                continue

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

            prevNode = curr

        print(res)

        return res
