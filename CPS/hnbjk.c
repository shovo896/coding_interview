#include<stdio.h> 
int main(){
    int n= 5 ;
    for (int i = 1 ; i<=n;i++){
        int spaces = n-i;
        while (spaces--){
            printf(" ");
        }
        for (int j=0 ;j<2*i-1;j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;   
    }
