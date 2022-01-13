"""
Lowest Common Ancestor of a Binary Search Tree
"""
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    
    que = deque([root])

    lcm = None

    while que:

        cur = que.popleft()

        if nodeInSubTree(cur, p) and nodeInSubTree(cur, q):
            lcm = cur
        
        if cur.left:
            que.append(cur.left)
        
        if cur.right:
            que.append(cur.right)
    
    return lcm



def nodeInSubTree(subRoot, node):
    
    q = deque([subRoot])

    while q:
        
        cur = q.popleft()

        if cur == node:
            return True

        if cur.left:
            q.append(cur.left)
        
        if cur.right:
            q.append(cur.right)
    
    return False



root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)


print(lowestCommonAncestor(root, root.right.left, root.right.right))






