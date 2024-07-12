#include <stdio.h>

int main() {
    
    int a , b , add , sub;

    scanf("%d %d" , &a , &b);

    add = a+b;
    sub = a-b;

    printf("%.2lf" , (double)add/sub);


    return 0;
}