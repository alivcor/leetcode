#include <iostream>
#include "map"
#include "vector"
#include "unordered_set"
using namespace std;

class Solution {
public:
    int distributeCandies(vector<int>& candies) {
        int numCandies = candies.size();
        std::map<int, int> candiesMap;
        for(auto it=candies.begin();it!=candies.end(); ++it) {
            if (candiesMap.find(*it) != candiesMap.end()) {
                candiesMap[*it] = 1;
            } else {
                candiesMap[*it] += 1;
            }
        };
        return min(numCandies/2, (int)candiesMap.size());
    }
    int optimized_distributeCandies(vector<int>& candies) {
        unordered_set<int> kinds;
        for (int kind : candies) {
            kinds.insert(kind);
        }
        return min(kinds.size(), candies.size() / 2);
    }

};

int main() {
    std::cout << "Hello, World!" << std::endl;
    Solution sol;
    vector<int> vector1{1,1,2,3};
    cout << sol.distributeCandies(vector1);
    return 0;
}