# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

longest_path=0
def longestUnivaluePath(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    global longest_path
    if not root: return 0
    longest_left = longestUnivaluePath(root.left)
    longest_right = longestUnivaluePath(root.right)
    if(root.left and root.val == root.left.val):
        longest_left = longest_left + 1
    if(root.right and root.val == root.right.val):
        longest_right = longest_right + 1
    longest_path= max(longest_path, longest_left + longest_right)
    return max(longest_left, longest_right)

