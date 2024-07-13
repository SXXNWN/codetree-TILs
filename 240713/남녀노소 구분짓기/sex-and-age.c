#include <stdio.h>

int main() {
    
    int s , n;

    scanf("%d %d" , &s , &n);

    if(s==0){

        if(n>=19){printf("%s" , "MAN");}
        else{printf("%s" , "BOY");}
    }

    else{
        
        if(n>=19){printf("%s" , "WOMAN");}
        else {printf("%s" , "GIRL");}
    }
    
    return 0;
}