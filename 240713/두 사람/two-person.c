#include <stdio.h>

int main() {
    int a1 , a2;
    char s1 , s2;

    scanf("%d %c %d %c" , &a1  ,&s1 , &a2 , &s2);

    if((a1>=19 && s1=='M') || (a2>=19 && s2 == 'M')) printf("%d" , 1);
    else printf("%d" , 0);


    return 0;
}