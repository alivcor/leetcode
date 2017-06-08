#include <iostream>
#include "vector"
#include "string"
using namespace std;

class Solution {
public:
    void printIntVector(vector<int>& nums){
        string s;
        for(auto it = nums.begin();it!=nums.end(); ++it){
            s.append(to_string(*it));
            s.append(", ");
        }
        std::cout << s.substr(0,s.length()-2);
    }
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int m = nums.size(); //current number of rows
        int n = nums[0].size(); //current number of cols
        int N = m*n;
        vector<vector<int>> res(r, vector<int>(c, 0));

        if(r*c!=N){ return nums;}
        else {
            for(int i = 0 ; i < N; i++){
                res[i/c][i%c] = nums[i/n][i%n];
            }
        }
        return res;
    }
};

int main() {
    std::vector<std::vector<int>> matrix {{1,2,3,4},{5,6,7,8},{9,10,11,12}, {13,14,15,16}};
    Solution sol;
    vector<vector<int>> newm = sol.matrixReshape(matrix, 2, 8);
    for(auto it=newm.begin();it!=newm.end();++it){
        sol.printIntVector(*it);
        cout << " \n";
    }
    return 0;
}