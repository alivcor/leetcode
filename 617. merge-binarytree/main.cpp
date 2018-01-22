#include <iostream>
#include "vector"

/**
 * Definition for a binary tree node.
 *
 * };
 */
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;

  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

using namespace std;

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {

    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    Solution sol;
    TreeNode tA1(52);
    TreeNode tA2(10);
    TreeNode tA3(56);


    TreeNode tB1(12);
    TreeNode tB2(7);
    TreeNode tB3(17);
    TreeNode tB4(10);
    TreeNode tB5(18);
    TreeNode tB6(15);

    tA1.left = &tA2;
    tA1.right = &tA3;

    tB1.left = &tB2;
    tB1.right = &tB3;
    tB3.left = &tB4;
    tB3.right = &tB5;
    tB5.left = &tB6;

    sol.mergeTrees(&tA1, &tB1);
    return 0;
}