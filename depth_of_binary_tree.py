from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):

    stack = [[root, 1]]
    res = 0

    while stack:

        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])

    return res


def maxDepth_recursively(root):
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


def maxDepth_iterative(root):
    if not root:
        return 0

    level = 0

    q = deque([root])

    while q:

        for i in range(len(q)):
            node = q.popleft()

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        level += 1
    return level


test_tree = TreeNode(3)

test_tree.left = TreeNode(9)
test_tree.right = TreeNode(20)

test_tree.left.left = TreeNode(2)
test_tree.left.left.left = TreeNode(1)


print(maxDepth(test_tree))
print(maxDepth_recursively(test_tree))
print(maxDepth_iterative(test_tree))
