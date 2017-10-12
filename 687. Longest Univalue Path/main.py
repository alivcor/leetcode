# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def longestUnivaluePath(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if(root.val == root.left.val and root.val == root.right.val):
        return(1 + max(longestUnivaluePath(root.left), longestUnivaluePath(root.right)))
    if(root.left.val == root.val):
        return 1 + longestUnivaluePath(root.left)
    elif(root.right.val == root.val):
        return 1 + longestUnivaluePath(root.right)
    else:
        return 1


