#include <stdio.h>

int main() {
    int n;
    scanf("%d" , &n);

    for(int i = 0 ; i < n ; i++){
        for(int j = i ; j < n ; j++){
            printf("*");
        }
        for(int j = 0 ; j < i*2 ; j++){
            printf(" ");
        }
        for(int j = i ; j < n ; j++){
            printf("*");
        }
        
        printf("\n");
        
    }
    return 0;
}