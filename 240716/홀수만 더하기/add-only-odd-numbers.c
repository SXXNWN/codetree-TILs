#include <stdio.h>

int main() {
    
    int n,x,sum=0;

    scanf("%d " , &n);

    for(int i=0;i<n;i++){

        scanf("%d " , &x);
        if(x%2!=0 && x%3==0){
            sum=sum+x;
        }
    
    printf("%d" , sum);
    }
    return 0;
}