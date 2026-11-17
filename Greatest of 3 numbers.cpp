#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c;
    cin >> a;
    cin >> b;
    cin >> c;

    // code here
    if (a > b && a > c) {
        cout << a;
        
    }
    if (b > a && b > c) {
        cout << b;
        
    }
    if (c > b && c > a) {
        cout << c;
        
    }
    return 0;
}
