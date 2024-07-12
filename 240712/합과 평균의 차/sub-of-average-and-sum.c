#include <stdio.h>

int main() {
    int a , b , c , sum;

    scanf("%d %d %d", &a , &b , &c);

    sum = a+b+c;

    printf("%d\n%d\n%d" , sum , sum/3 , sum-(sum/3));

    return 0;
}