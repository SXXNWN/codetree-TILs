#include <stdio.h>

int main() {
    
    char s[100];

    scanf("%s" , s);     //&가 없는 이유: 배열이름 자체가 주소이기 때문
    printf("%s" , s);
    
    return 0;
}