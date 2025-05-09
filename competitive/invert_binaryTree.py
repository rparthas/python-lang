from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.left,root.right = right,left
        return root


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    solution = Solution()
    inverted_root = solution.invertTree(root)
    res = []
    queue = deque([root])
    while queue:
        val = queue.popleft()
        res.append(val.val)
        if val.left:
            queue.append(val.left)
        if val.right:
            queue.append(val.right)
    print(res)
