#include <iostream>
#include "vector"
#include "cmath"
using namespace std;

class Solution {
public:
    vector<bool> dec2bin(int num) {
        vector<bool> bin_num;
        while(num!=0){
            bool rem = num % 2;
            num /= 2;
            bin_num.insert(bin_num.begin(), rem);
        }
        return bin_num;
    }
    int bin2dec(vector<bool> bin_num){
        int num=0;
        for(int i=0;i<bin_num.size();i++){
            if(bin_num[i] == 1) {
                num += pow(2, (bin_num.size()-i-1));
            }
        }
        cout<<endl;
        return num;
    }
    int findComplement(int num) {
        vector<bool> bin_num = dec2bin(num);
        for(int i=0;i<bin_num.size();i++){
            cout << bin_num[i];
        }
        cout << endl;
        for(int i=0;i<bin_num.size();i++){
            if(bin_num[i] == 0){
                bin_num[i] = 1;
            } else {
                bin_num[i] = 0;
            }
        }
        for(int i=0;i<bin_num.size();i++){
            cout << bin_num[i];
        }
        cout << endl;
        return bin2dec(bin_num);
    }
};
int main() {
    Solution sol;
    cout << sol.findComplement(5);
    return 0;
}