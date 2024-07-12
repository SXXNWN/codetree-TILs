#include <stdio.h>

int main() {
    int a;

    scanf("%d" , &a);

    if(a%13==0 || a%19==0) printf("%s" , "True");
    else printf("%s" , "False");

    return 0;
}