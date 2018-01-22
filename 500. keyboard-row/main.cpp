#include <iostream>
#include "vector"
#include "string"

using namespace std;

class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        string listA = "QWERTYUIOP";
        string listB = "ASDFGHJKL";
        string listC = "ZXCVBNM";
        vector<string> goodwords;
        int belongsto = 0;

        for(auto it=words.begin();it!=words.end();++it){
            belongsto = 0;
            bool good = true;
            for(int i = 0; i < (*it).length(); i++){
                if(belongsto == 0) {
                    if (listA.find((char)toupper((*it)[i]))!=std::string::npos) {
                        belongsto = 1;
//                        cout << *it << " belongsto " << belongsto << endl;
                    } else {
                        if (listB.find((char)toupper((*it)[i]))!=std::string::npos) {
                            belongsto = 2;
//                            cout << *it << " belongsto " << belongsto << endl;
                        } else {
                            if (listC.find((char)toupper((*it)[i]))!=std::string::npos) {
                                belongsto = 3;
//                                cout << *it << " belongsto " << belongsto << endl;
                            }
                        }
                    }
                } else {
                    if (listA.find((char)toupper((*it)[i]))!=std::string::npos && belongsto != 1) {
//                        cout << *it << " << Not good ! mismatch " << (char)toupper((*it)[i]) << endl;
                        good = false;
                        break;
                    } else {
                        if (listB.find((char)toupper((*it)[i]))!=std::string::npos && belongsto != 2) {
//                            cout << *it << " << Not good ! mismatch " << (char)toupper((*it)[i]) << endl;
                            good = false;
                            break;
                        } else {
                            if (listC.find((char)toupper((*it)[i]))!=std::string::npos && belongsto != 3) {
//                                cout << *it << " << Not good ! mismatch " << (char)toupper((*it)[i]) << endl;
                                good = false;
                                break;
                            }
                        }
                    }
                }
            }
            if(good){
                goodwords.insert(goodwords.end(), *it);
            }

        }
        return goodwords;
    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    std::vector<string> s({"Alaska", "Great", "GAS"});
    Solution sol;
    vector<string> goodwords = sol.findWords(s);
    for(auto it=goodwords.begin();it!=goodwords.end();++it){
        cout<<*it<<endl;
    }
    return 0;
}