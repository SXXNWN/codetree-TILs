#include <stdio.h>

int main() {
    int a , b , c;

    scanf("%d %d %d" , &a , &b , &c);

    if(a>b){                                  
        if(a>c){
            if(b>c){printf("%d" , b);}
            else if(b<c) {printf("%d" , c);}
        }
        else if(a<c){printf("%d" , a);}
    }

    else if(b>a){                             
        if(b>c){
            if(a>c){printf("%d" , a);}
            else if(a<c) {printf("%d" , c);}
        }
        else if(b<c){printf("%d" ,b);}
    }  

    else if(c>a){                              
        if(c>b){
            if(a>b){printf("%d" , a);}
            else if(a<b){printf("%d" , b);}
        }
        else if(c<b){printf("%d" , c);}
    }                           
    return 0;
}