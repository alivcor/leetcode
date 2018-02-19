from binarytree import tree


## Using Recursion
class RecursivePaths:

    def dfs(self, node, ls, res):
        if not node.left and not node.right:
            res.append(ls + str(node.value))
        if node.left:
            self.dfs(node.left, ls + str(node.value) + "->", res)
        if node.right:
            self.dfs(node.right, ls + str(node.value) + "->", res)


    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return ""
        res = []
        self.dfs(root, "", res)
        return res


class DFSUsingStack:
    def binaryTreePaths(self, root):
        if not root:
            return ""
        res = []
        stack = [] # BOT 0 1 2 3 TOP
        stack.append([root, ""])
        while(stack):
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.value))
            if node.right:
                stack.append([node.right, ls + str(node.value) + "->"])
            if node.left:
                stack.append([node.left, ls + str(node.value) + "->"])
        return res


# class BFSUsingQueue:



# Generate a random binary tree and return its root node
my_tree = tree(height=3, is_perfect=False)
print(my_tree)

method_1 = RecursivePaths()
print method_1.binaryTreePaths(my_tree)

method_2 = DFSUsingStack()
print method_2.binaryTreePaths(my_tree)