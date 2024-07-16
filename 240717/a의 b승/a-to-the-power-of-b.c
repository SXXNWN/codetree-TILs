#include <stdio.h>

int main() {
    int a , b , x = 1;

    scanf("%d %d" , &a , &b);

    for(int i = 1 ; i <=b ; i++){
        x *= a;
    }

    printf("%d" , x);

    return 0;
}