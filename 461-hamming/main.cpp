#include <iostream>
#include <vector>


class Solution {
public:
    std::vector<bool> dec2bin(int num){
        std::vector<bool> bin_num;
        while(num!=0){
            bool rem = num%2;
            num /= 2;
            bin_num.insert(bin_num.begin(), rem);
        };
        std::copy(bin_num.begin(), bin_num.end(), std::ostream_iterator<char>(std::cout, " "));

        return bin_num;
    }
    int hammingDistance(int x, int y) {
        std::vector<bool> bx = dec2bin(x);
        std::vector<bool> by = dec2bin(y);
    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    Solution sol;
    std::cout << sol.hammingDistance(101,1002);
    return 0;
}