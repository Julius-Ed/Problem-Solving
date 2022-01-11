from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def isSubtree(root, subRoot) -> bool:
        
    if not root:
        return False
        
    q = deque([root])

    while q:

        current = q.popleft()

        if current.left:
            q.append(current.left)
            
        if current.right:
            q.append(current.right)
            
        if current.val == subRoot.val:
            if isSameTree_recursive(current, subRoot):
                return True
    
    return False

def isSubtree_recursive(root, subRoot):

    if not root:
        return False
    
    if isSameTree_recursive(root, subRoot) or isSubtree_recursive(root.left, subRoot) or isSubtree_recursive(root.right, subRoot):
        return True
    
    return False


def isSameTree_recursive(p, q):
    if p == None and q == None:
        return True

    if p == None and q != None:
        return False

    if q == None and p != None:
        return False

    if p.val != q.val:
        return False
    
    if p == None and q == None:
        return True

    return isSameTree_recursive(p.left, q.left) and isSameTree_recursive(p.right, q.right)