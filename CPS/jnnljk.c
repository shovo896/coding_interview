#include<stdio.h>
int main(){
    int n ;
    scanf("%d", &n);
    while (n>9){
        int x = n ; 
        int sum = 0 ;
        while (x!= 0){
            int last = x%10 ;
            sum = sum + last ;
            x = x/10 ;
        }
        n = sum ;
    }
    printf("%d\n", n);
    return 0 ;
}