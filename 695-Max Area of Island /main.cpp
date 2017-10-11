#include <iostream>
#include "map"
#include "vector"
#include "unordered_set"
using namespace std;


class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
//        cout << grid;
        return 0;
    }
};

int main() {
//    std::cout << "Hello, World!" << std::endl;
    vector<vector<int>> grid {{0,0,1,0,0,0,0,1,0,0,0,0,0},
                              {0,0,0,0,0,0,0,1,1,1,0,0,0},
                              {0,1,1,0,1,0,0,0,0,0,0,0,0},
                              {0,1,0,0,1,1,0,0,1,0,1,0,0},
                              {0,1,0,0,1,1,0,0,1,1,1,0,0},
                              {0,0,0,0,0,0,0,0,0,0,1,0,0},
                              {0,0,0,0,0,0,0,1,1,1,0,0,0},
                              {0,0,0,0,0,0,0,1,1,0,0,0,0}};
    Solution sol;
    cout << sol.maxAreaOfIsland(grid);
    return 0;
}