#include <stdio.h>
#include <stdbool.h>

int main() {

    int n;
    
    bool x = true;

    scanf("%d" , &n);

    for(int i = 2 ; i<n ; i++){
        if(n%i==0) x = false;
    }

    if(x==true) printf("P");
    else printf("C");

    return 0;
}