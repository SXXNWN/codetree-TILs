#include <stdio.h>

int main() {
    int cnt = 0;
    int n;
    scanf("%d" , &n);
    while(1){
        if(n%2==0){
            n/=2;
            cnt++;
        }

        else if(n==1){
            printf("%d" , cnt);
            break;
        }   
        else if(n%2==1){
            n = n*3+1;
            cnt++;
        }

        
    }
    return 0;
}