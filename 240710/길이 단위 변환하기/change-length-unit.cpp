#include <iostream>

using namespace std;

int main() {
    
    double a = 30.48;
    int b = 160934; 

    cout << fixed;
    cout.precision(1);

    cout << "9.2ft = " << a*9.2 << "cm" <<  endl;
    cout << "1.3mi = " << b*1.3 << "cm";

    return 0;
}