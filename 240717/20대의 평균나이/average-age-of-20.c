#include <stdio.h>

int main() {
    
    int cnt = 0 , sum = 0;

    while(1){
        int n ;

        scanf("%d" , &n);

        if(n<30 && n>19){
        sum += n;
        cnt++;
        }

        else
            break;
    }

    printf("%.2lf" , (double)sum/cnt);
    return 0;
}