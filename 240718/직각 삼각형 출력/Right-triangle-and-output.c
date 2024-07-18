#include <stdio.h>

int main() {
    int n;
    scanf("%d" , &n);

    for(int i = 1 ; i <= n ; i++){
        int j = (i*2) - 1;
        for(; j > 0 ; j--){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}