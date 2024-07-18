#include <stdio.h>
#include <stdbool.h>

int main() {
    int a , b , c , d , e;
    bool x = true;

    scanf("%d %d %d %d %d" , &a , &b , &c , &d , &e);

    if(a%3!=0 || b%3!=0 || c%3!=0 || d%3!=0 || e%3!=0) x = false;

    if(x==true) printf("1");
    else printf("0");
    
    return 0;
}