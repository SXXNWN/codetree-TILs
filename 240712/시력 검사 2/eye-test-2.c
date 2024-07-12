#include <stdio.h>

int main() {
    double a;

    scanf("%lf" , &a);

    if(a<0.5) printf("%s" , "Low");
    else if(a<1.0) printf("%s" , "Middle");
    else printf("%s" , "High");

    return 0;
}