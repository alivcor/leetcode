#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int hammingDistance(int x, int y) {
        int dist = 0, num = x^y;
        //loop is for counting the number of set bits in num (x^y)
        while(num){
            dist++; //how may bits we have turned off(set to 0)
            num &= num-1; // set the rightmost bit to zero
        }
        return dist;

    }
};

int main() {
    cout << "Hello, World!" << std::endl;
    Solution sol;
    int dist = sol.hammingDistance(101,4);
    cout << dist;
    return 0;
}