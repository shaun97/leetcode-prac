# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we use dfs to search for the starting root of the subroot
        # once we found a node that has the same value as the subroot, we do a match

        q = deque()
        q.append(root)
        visited = set()

        while q:
            node = q.pop()
            if node.val == subRoot.val:
                # dfs match
                matchQueue = deque()
                matchQueue.append((node, subRoot))
                isFound = True

                while matchQueue:
                    cNode, sNode = matchQueue.pop()
                    if cNode.val != sNode.val:
                        isFound = False
                        break

                    # handle none case
                    if sNode.left:
                        if cNode.left == None:
                            isFound = False
                            break
                        else:
                            matchQueue.append((cNode.left, sNode.left))
                    else:
                        if cNode.left != None:
                            isFound = False
                            break

                    if sNode.right:
                        if cNode.right == None:
                            isFound = False
                            break
                        else:
                            matchQueue.append((cNode.right, sNode.right))
                    else:
                        if cNode.right != None:
                            isFound = False
                            break
                if isFound:
                    return True

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False
