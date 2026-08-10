#include<stdio.h>
int f(int x ){
    int ans = 3*x + 2 ;
    return ans ;
}
int main(){
    int test = f(4);
    printf("%d\n",test);
    return 0 ;
}