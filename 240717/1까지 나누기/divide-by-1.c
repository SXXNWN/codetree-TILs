#include <stdio.h>

int main() {
    int n;

    scanf("%d" , &n);

    int a=n;

    for(int i=1 ; i<=n ; i++){
        a/=i;
        if(a<=1){
            printf("%d" , i);
            break;
        }
    }
    return 0;
}