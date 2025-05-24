# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        self.stack.append(root)
        self.visited = set()

    def next(self) -> int:
        while self.stack:
            node = self.stack.pop()

            if node not in self.visited:
                if node.right:
                    self.stack.append(node.right)
            # in order traversal, since we are using the stack, we push the right, itself and left
                self.stack.append(node)
                if node.left:
                    self.stack.append(node.left)
                self.visited.add(node)
            else:
                return node.val

    def hasNext(self) -> bool:
        if self.stack:
            return True
        else:
            return False
