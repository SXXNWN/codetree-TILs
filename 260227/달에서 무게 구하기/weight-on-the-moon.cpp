#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    cout << fixed;
    
    int a = 13;
    double b = 0.165;

    cout.percision(6);

    cout << a << " * " << b << " = " << a*b;

    return 0;
}