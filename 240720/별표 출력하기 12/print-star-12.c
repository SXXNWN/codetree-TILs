#include <stdio.h>

int main() {
    int n;
    scanf("%d" , &n);

    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < n ; j++){
            if(i==0)printf("* ");
            else{
                if(i%2==0 && i==j) printf("* ");
            }
        }
        printf("\n");
    }
    return 0;
}