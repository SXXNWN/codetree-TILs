#include <stdio.h>

int main() {
    int a;

    scanf("%d" , &a);

    if(a==5) printf("%c" , 'A');
    if(a%2==0) printf("%c" , 'B');
    
    return 0;
}