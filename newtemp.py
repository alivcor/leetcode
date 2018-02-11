# Binary Tree Level Order
def binaryTreeLevelOrder(root):
    if root == None:
        return None

    q = Queue.LifoQueue()
    q.put(root)

    while(not q.empty()):
        node_out = q.get()
        print node_out.val
        if node_out.left != None: q.put(node_out.left)
        if node_out.right != None: q.put(node_out.right)


# Binary Tree Paths
public List<String> binaryTreePaths(TreeNode root) {
    List<String> answer = new ArrayList<String>();
    if (root != null) searchBT(root, "", answer);
    return answer;
}
private void searchBT(TreeNode root, String path, List<String> answer) {
    if (root.left == null && root.right == null) answer.add(path + root.val);
    if (root.left != null) searchBT(root.left, path + root.val + "->", answer);
    if (root.right != null) searchBT(root.right, path + root.val + "->", answer);
}


#GCD
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


# Two Sum
def twoSum(self, nums, target):
    hashmap = dict()
    lennums = len(nums)
    for i in xrange(lennums):
        num = nums[i]
        complement = target - num
        if complement in hashmap and hashmap[complement] != i:
            return i, hashmap[complement]
        hashmap[num] = i


#Reverse Integer
def reverse(self, x):
    if (x < 0):
        y = -1 * int((str(x)[1:])[::-1])
    else:
        y = int(str(x)[::-1])
    if (abs(y) > (2 ** 31 - 1)):
        return 0
    else:
        return y


# Merge Two Sorted Lists
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
