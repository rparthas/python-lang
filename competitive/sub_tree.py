from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.findSubTree(root,subRoot,False)

    def findSubTree(self,root: Optional[TreeNode], subRoot: Optional[TreeNode], matched:bool) -> bool:
        if root and subRoot:
            if root.val == subRoot.val:
                return (
                    self.findSubTree(root.left,subRoot.left, True) and
                    self.findSubTree(root.right,subRoot.right, True)
                )
            else:
                if matched:
                    return False
                else:
                    return (
                        self.findSubTree(root.left,subRoot,False) or
                        self.findSubTree(root.right,subRoot,False)
                    )


        if not root and subRoot:
            return False

        return matched

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)

    subRoot = TreeNode(2)
    subRoot.left = TreeNode(4)
    subRoot.right = TreeNode(5)

    solution = Solution()
    print(solution.isSubtree(root, subRoot))  # Output: False
