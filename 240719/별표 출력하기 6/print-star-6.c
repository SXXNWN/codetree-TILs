#include <stdio.h>

int main() {
    int n;
    scanf("%d" , &n);

    for(int i = 0 ; i < n ; i++){

        for(int j = 0 ; j < i ; j++){
            printf("  ");
        }
        for(int j = n*2 - 1 ; j > i*2 ; j--){
            printf("* ");
        }
        
        printf("\n");
    }

    for(int i = 1 ; i < n ; i++){
        for(int j = n ; j > i + 1 ; j--){
            printf("  ");
        }
        for(int j = 0 ; j < i * 2 + 1 ; j++){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}