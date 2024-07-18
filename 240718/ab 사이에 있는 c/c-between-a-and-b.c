#include <stdio.h>
#include<stdbool.h>

int main() {
    
    int a , b , c;
    bool x = false;

    scanf("%d %d %d" , &a , &b , &c);

    for(int i = a ; i <= b ; i++){
        if(i%c==0){
            x = true ; 
        }
    }

    if(x==true) printf("YES");
    else printf("NO");

    return 0;
}