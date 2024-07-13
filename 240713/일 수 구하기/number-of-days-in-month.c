#include <stdio.h>

int main() {
    
    int n;

    scanf("%d" , &n);

    if(n%2 != 0) printf("%d" , 31);
    
    else{

        if(n==2){printf("%d" , 28);}

        else{ printf("%d" , 30);}
    }
    return 0;
}