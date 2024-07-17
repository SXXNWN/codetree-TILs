#include <stdio.h>

int main() {
    
    while(1){
        int a , b;
        char x;

        scanf("%d %d %c" , &a , &b , &x);

        printf("%d\n" , a*b);

        if(x=='C')
            break;
    }
    return 0;
}