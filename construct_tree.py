"""
Construct a binary tree given a list of preOrder and inOrder values
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def tree(preOrder, inOrder):

    if len(inOrder) == 0:
        return None
    

    root = TreeNode(preOrder.pop(0))

    left = tree(preOrder, inOrder[:inOrder.index(root.val)])
    right = tree(preOrder, inOrder[inOrder.index(root.val) + 1:])

    root.left = left
    root.right = right

    return root
