#include <stdio.h>

int main() {
    
    int a , b;
    int sum = 0 , cnt = 0;

    scanf("%d %d" , &a , &b);

    for(int i = a ; i <= b ; i++){

        if(i%5 == 0 || i%7 == 0){
            sum+=i;
            cnt++;
        }
    }

    
    printf("%d %.1lf" , sum , (double)sum/cnt);

    return 0;
}