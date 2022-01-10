class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree_iterative(p, q):

    queue_p = [p]
    queue_q = [q]

    while queue_p and queue_q:

        current_p = queue_p.pop(0)
        current_q = queue_q.pop(0)

        if current_p == None and current_q != None:
            return False

        if current_q == None and current_p != None:
            return False

        if current_p == None and current_q == None:
            continue

        if current_p.val != current_q.val:
            return False

        queue_p.append(current_p.left)
        queue_p.append(current_p.right)

        queue_q.append(current_q.left)
        queue_q.append(current_q.right)

    return True


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


tree_p = TreeNode(1)
tree_p.left = TreeNode(0)
tree_p.right = TreeNode(2)
tree_p.left.left = TreeNode(4)

tree_q = TreeNode(1)
tree_q.left = TreeNode(0)
tree_q.right = TreeNode(2)