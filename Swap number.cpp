#include <bits/stdc++.h>
using namespace std;

int main (){
    int a;
    std::cin >> a;


    int b;
    std::cin >>b;

    int c = a;
    a = b;
    b = c;

    std::cout << a << " " << b;
    return 0;
}