#include <stdio.h>

int main() {
    
    int n,sum=0;

    scanf("%d " , &n);

    for(int i=0;i<n;i++){
        int x;
        scanf("%d " , &x);
        if(x%2!=0 && x%3==0){
            sum+=x;
        }
    
    printf("%d" , sum);
    }
    return 0;
}