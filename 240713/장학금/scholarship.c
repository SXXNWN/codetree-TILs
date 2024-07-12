#include <stdio.h>

int main() {
    int a,b;

    scanf("%d %d" , &a , &b);

    if(a<90) printf("%d" , 0);
    else if(b>=95) printf("%d" , 100000);
    else if(b>=90) printf("%d" , 50000);
    else printf("%d" , 0);
    
    return 0;
}