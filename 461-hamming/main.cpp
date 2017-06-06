#include <iostream>
#include <vector>


class Solution {
public:
    std::vector<bool> dec2bin(int num){
        std::vector<bool> bin_num;
        bool rem;
        while(num!=0 && (num!=1 || rem!=1)){
            std::cout << " \n";
            for(int i = 0; i < bin_num.size(); i++){
                std::cout << bin_num[i];
            }
            rem = num%2;
            num /= 2;
            std::cout << "**";
            bin_num.insert(bin_num.begin(), rem);
            for(int i = 0; i < bin_num.size(); i++){
                std::cout << bin_num[i];
            }
        };
//        for (auto i = bin_num.begin(); i != bin_num.end(); ++i)
//            std::cout << *i;
        std::cout << " \n";
        for(int i = 0; i < bin_num.size(); i++){
            std::cout << bin_num[i];
        }

        return bin_num;
    }
    std::string toBinary(int n)
    {
        std::string r;
        while(n!=0) {r=(n%2==0 ?"0":"1")+r; n/=2;}
        return r;
    }
    int hammingDistance(int x, int y) {
        std::string bx = toBinary(x);
        std::cout << bx;
        std::cout << "\n ---- \n";
        std::string by = toBinary(y);
        std::cout << by;
    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    Solution sol;
    std::cout << sol.hammingDistance(101,4);
    return 0;
}