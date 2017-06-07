#include <iostream>
#include "vector
using namespace std;

class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        std::vector<std::vector<int>> res_m;
        std::vector<int> all_elem;
        for(auto it1 = nums.begin(); it1 != nums.end(); it1++){
            for(auto it2 = (*it1).begin(); it2 != (*it1).end(); it2++) {
                all_elem.insert(all_elem.end(), *it2);
            }
        }
        for(int i = 0; i < all_elem.size(); i++){

        }

    }
};

int main() {
    std::vector<std::vector<int>> matrix {{1,2,3,4},{5,6,7,8},{9,10,11,12}, {13,14,15,16}};
    return 0;
}