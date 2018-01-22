#include <iostream>
#include "vector"

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        size_t front = 0;
        for(int i = 0; i<=s.length(); i++){
            if(s[i] == ' ' || i == s.length()){
                reverse(&s[front], &s[i]); // reverse the last traversed word
                front = i + 1; // 1 is for space
            }
        }
        return s;
    }
};
int main() {
    Solution sol;
    cout << sol.reverseWords(std::string ("Abhinandan Dubey"));
    return 0;
}