#include <iostream>
#include "vector"
using namespace std;

class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        int maxSum = 0;
        int holder = 0;
        std::sort(nums.begin(), nums.end());
        std::reverse(nums.begin(),nums.end());
        std::vector<int> pairs;
        bool insFlag = true;
        for(auto it = nums.begin(); it != nums.end(); ++it){
            if(insFlag){
                cout<<"Storing "<<*it<<" \n";
                holder = *it;
                insFlag = false;
            } else {
                pairs.insert(pairs.begin(), min(holder,*it));
                insFlag = true;
            }
        }
//        for(auto it = pairs.begin(); it!=pairs.end(); ++it){
//            cout << *it;
//            cout << " ";
//        }
        for(std::vector<int>::iterator it = pairs.begin(); it != pairs.end(); ++it)
            maxSum += *it;
        return maxSum;
    }
};

int main() {
    Solution sol;
    int myints[] = {1,4,3,2};
    std::vector<int> myvector (myints, myints+4);
    sol.arrayPairSum(myvector);
    return 0;
}