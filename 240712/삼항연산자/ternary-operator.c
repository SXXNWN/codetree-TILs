#include <stdio.h>

int main() {
    int a,b;
    

    scanf("%d",&a);

    b = a==100 ? 0 : 1;

    if(b==0) printf("%s" , "pass");
    else printf("%s" , "failure");

    return 0;
}