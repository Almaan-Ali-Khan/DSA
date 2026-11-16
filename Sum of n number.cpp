#include <bits/stdc++.h>
#include <numeric>
#include <list>
using namespace std;

class Solution {
    public:
        int sumOfDigits(int n) {
            std::list<int> L;
    

            while (n > 0) {
                int i = n % 10;
                L.push_back(i);
                n /= 10;
            }
    

            int sum = std::accumulate(L.begin(), L.end(), 0);
            return sum;
    }
};