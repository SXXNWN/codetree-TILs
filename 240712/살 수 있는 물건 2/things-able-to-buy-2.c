#include <stdio.h>

int main() {
    int n;

    scanf("%d" , &n);

    if(n>=3000) printf("%s" , "book");
    else if(n>=1000) printf("%s" , "mask");
    else if(n>=500) printf("%s" , "pen");
    else printf("%s" , "no");
    
    return 0;
}