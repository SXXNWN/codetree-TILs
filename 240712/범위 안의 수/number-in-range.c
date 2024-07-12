#include <stdio.h>

int main() {
    int a;

    scanf("%d" , &a);

    if(a>=10 && a<=20) printf("%s" , "yes");
    else printf("%s" , "no");

    return 0;
}