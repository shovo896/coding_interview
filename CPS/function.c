#include<stdio.h>
int f(int x ){
    int ans = 3*x + 2 ;
    return ans ;
}

// double 
double d(double y ){
    return y/2 ; 
}
int main(){
    int test = f(4);
    printf("%d\n",test);
    double test2 = d(4.0);
    printf("%f\n",test2);
    return 0 ;
}