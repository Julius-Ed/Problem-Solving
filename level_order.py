
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def levelOrder(root):
    if not root:
        return []

    result = list()

    queue = deque([(root,  0)])

    while queue:
        root, level = queue.popleft()

        if not root:
            continue
        if len(result) == level:
            result.append([])

        result[level].append(root.val)

        queue.append((root.left, level + 1))
        queue.append((root.right, level + 1))

    return result

tree = TreeNode(1)

tree.left = TreeNode(2)
tree.right = TreeNode(3)

tree.left.left = TreeNode(4)

tree.right.right = TreeNode(5)



