#include <stdio.h>

int main() {
    double a,b;
    char s;

    scanf("%c %lf %lf" , &s , &a , &b);
    printf("%c\n%.2lf\n%.2lf" , s , a , b);

    return 0;
}