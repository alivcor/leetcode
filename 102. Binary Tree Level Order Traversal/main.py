from binarytree import tree
import Queue

# Generate a random binary tree and return its root node
my_tree = tree(height=3, is_perfect=False)

print(my_tree)


def binaryTreeLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if root == None:
        return None

    q = Queue.LifoQueue()
    q.put(root)

    while(not q.empty()):
        node_out = q.get()
        print node_out.val
        if node_out.left != None: q.put(node_out.left)
        if node_out.right != None: q.put(node_out.right)

