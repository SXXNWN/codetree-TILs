#include <stdio.h>

int main() {
    
    int h,w,bmi;
    
    scanf("%d %d" , &h , &w);

    bmi = w*100*100/(h*h);
    
    printf("%d\n" , bmi);

    if(bmi>=25) printf("%s" , "Obesity" );

    return 0;
}