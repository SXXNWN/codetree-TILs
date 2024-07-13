#include <stdio.h>

int main() {
    
    int n;

    scanf("%d" , &n);

    if(n==2) printf("%d" , 28); //46911 30
    
    if(n==4 || n==6 || n==9 || n==11) printf("%d" , 30);
    else printf("%d" , 31);
    
    return 0;
}