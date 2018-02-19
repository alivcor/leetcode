from binarytree import tree
import Queue


def binaryTreeLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if root == None:
        return []

    q = Queue.Queue()
    q.put(root)

    mainList = []
    while(not q.empty()):
        level_num = q.qsize()
        # print "level_num =", level_num,
        sublist = []
        for i in xrange(level_num):
            node_out = q.get()
            # print "i =", i, " | node_out.value =", node_out.value, " | queue = ", list(q.queue),
            if node_out.left != None: q.put(node_out.left)
            if node_out.right != None: q.put(node_out.right)
            sublist.append(node_out.value)
            # print " | subList: ", sublist
        mainList.append(sublist)
    return mainList


# Generate a random binary tree and return its root node
my_tree = tree(height=2, is_perfect=True)

print(my_tree)

print(binaryTreeLevelOrder(my_tree))

