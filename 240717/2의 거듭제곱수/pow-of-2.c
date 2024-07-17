#include <stdio.h>

int main() {
    int n , cnt=0;

    scanf("%d" , &n);

    while(1){
        n/=2;
        cnt++;

        if(n/2==0) break;
        
    }
    printf("%d" , cnt);

    return 0;
}