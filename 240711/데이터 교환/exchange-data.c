#include <stdio.h>

int main() {
    int a = 5, b = 6, c = 7;
    int temp , ch;

    temp = a;
    ch = b;

    a = c;
    b = temp;
    c = ch;

    printf("%d\n", a);
    printf("%d\n", b);
    printf("%d", c);


    


    return 0;
}