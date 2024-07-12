#include <stdio.h>

int main() {
    int a,b;

    scanf("%d %d" , &a , &b);

    if(a%2==0) printf("%s\n" , "even");
    else printf("%s\n" , "odd");

    if(b%2==0) printf("%s" , "even");
    else printf("%s" , "odd");
    
    return 0;
}