
def findSecondMinimumValue(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def dfs(node):
        if node:
            uniques.add(node.val)
            dfs(node.left)
            dfs(node.right)

    uniques = set()
    dfs(root)
    minv = float("inf")
    sminv = float("inf")
    print uniques
    for x in uniques:
        if x < minv:
            sminv = minv
            minv = x
        elif minv < x < sminv:
            sminv = x
        print x, minv, sminv

    return sminv if sminv != float("inf") else -1