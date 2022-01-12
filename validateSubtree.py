"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root) -> bool:

    return valid(root, float("-inf"), float("inf"))


def valid(node, left, right):
    if not node:
        return True

    if not (node.val < right and node.val > left):
        return False

    return (valid(node.left, left, node.val) and valid(node.right, node.val, right))


root = TreeNode(5)

root.left = TreeNode(1)
root.right = TreeNode(6)

root.right.left = TreeNode(4)
root.right.right = TreeNode(7)


root_simple = TreeNode(5)

root_simple.left = TreeNode(1)
root_simple.right = TreeNode(7)

root_simple.right.left = TreeNode(6)
root_simple.right.right = TreeNode(8)


print(isValidBST(root))
