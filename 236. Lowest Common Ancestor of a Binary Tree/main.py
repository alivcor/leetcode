from random import randint
from binarytree import tree, bst, heap

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root in (None, p, q): return root
    left, right = (lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
    return right if left is None else left if right is None else root


# Generate a random binary tree and return its root node
my_tree = tree(height=3, is_perfect=False)

# Generate a random BST and return its root node
my_bst = bst(height=3, is_perfect=True)

print(my_tree)

print(lowestCommonAncestor(my_tree, my_tree.left.left, my_tree.left.right))
