#include <stdio.h>

int main() {
    int a;

    scanf("%d" , &a);

    if(a%3==0) printf("%s\n" , "YES");
    else printf("%s\n" , "NO");

    if(a%5==0) printf("%s" , "YES");
    else printf("%s" , "NO");
    
    return 0;
}