#include <stdio.h>

int main() {
    int a,b;  //a=가로 , b=세로

    scanf("%d %d" , &a , &b);

    a+=8;
    b*=3;

    printf("%d\n%d\n%d" , a , b , a*b);
    
    return 0;
}