#include <stdio.h>

int main() {
    int n;

    scanf("%d" , &n);

    printf("%d\n" , n);

    if(n<0){
        
        printf("%s" , "minus");
    }
    return 0;
}