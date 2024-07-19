#include <stdio.h>

int main() {
    int n;
    scanf("%d" , &n);

    for(int i = 0 ; i < n ; i++){                       //세로 줄
        for(int j = 0 ; j < n-i-1 ; j++){               //공백
            printf("  ");
        }
        for(int j = 0 ; j < 2*i + 1 ; j++){                 //별
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}