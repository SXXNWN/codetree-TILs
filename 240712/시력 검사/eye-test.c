#include <stdio.h>

int main() {
    double a , b;

    scanf("%lf %lf" , &a , &b);

    if(a>=1.0 && b>=1.0) printf("%s" , "High");
    else if(a>=0.5 && b>=0.5) printf("%s" , "Middle");
    else printf("%s" , "Low");

    return 0;
}