#include <stdio.h>

int main() {
    int a,b,c,d;

    scanf("%d %d %d %d" , &a , &b , &c ,&d);

    if(a>c) printf("%c" , 'A');
    else if(a<c) printf("%c" , 'B');
    else if(b>d) printf("%c" , 'A');
    else printf("%c" , 'B');
    
    return 0;
}