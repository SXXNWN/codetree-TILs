#include <stdio.h>

int main() {
    int dd , mm , yyyy;

    scanf("%d-%d-%d", &mm , &dd , &yyyy);
    printf("%d.%d.%d" , yyyy, mm, dd);
    
    return 0;
}