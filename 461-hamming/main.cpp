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
        return bin_num;
    }
    int hammingDistance(int x, int y) {
        std::vector<bool> bx = dec2bin(x);
        for(auto i = bx.begin(); i!=bx.end(); ++i){
            std::cout<<*i;
        }
        std::cout << "\n ---- \n";
        std::vector<bool> by = dec2bin(y);
        for(auto i = by.begin(); i!=by.end(); ++i){
            std::cout<<*i;
        }
    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    Solution sol;
    sol.hammingDistance(101,4);
    return 0;
}