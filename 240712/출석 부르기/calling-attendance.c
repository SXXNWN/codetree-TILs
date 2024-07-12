#include <stdio.h>

int main() {
    int a;

    scanf("%d" , &a);

    if(a==1) printf("%s" , "John");
    else if(a==2) printf("%s" , "Tom");
    else if(a==3) printf("%s" , "Paul");
    else printf("%s" , "Vacancy");
    
    return 0;
}