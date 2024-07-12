#include <stdio.h>

int main() {
    int n;

    scanf("%d" , &n);

    printf("%d\n" , n*n);

    if(n<5) printf("%s" , "tiny");
    
    return 0;
}