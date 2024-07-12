#include <stdio.h>

int main() {
    int m;

    scanf("%d" , &m);

    if(m>=3 && m<=5) printf("%s" , "Spring");
    else if(m>=6 && m<=8) printf("%s" , "Summer");
    else if(m>=9 && m<=11) printf("%s" , "Fall");
    else printf("%s" , "Winter");
    return 0;
}