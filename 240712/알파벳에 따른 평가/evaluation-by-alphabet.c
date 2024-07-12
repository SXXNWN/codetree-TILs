#include <stdio.h>

int main() {
    char a;

    scanf("%c" , &a);

    if(a=='S') printf("%s" , "Superior");
    else if(a=='A') printf("%s" , "Excellent");
    else if(a=='B') printf("%s" , "Good");
    else if(a=='C') printf("%s" , "Usually");
    else if(a=='D') printf("%s" , "Effort");
    else printf("%s" , "Failure");
    
    return 0;
}