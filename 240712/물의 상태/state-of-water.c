#include <stdio.h>

int main() {
    int n;

    scanf("%d" , &n);

    if(n<0) printf("%s" , "ice");
    else if(n>=100) printf("%s" , "vapor");
    else printf("%s" , "water");
    
    return 0;
}