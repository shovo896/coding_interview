#include<stdio.h>
int f(int x ){
    int ans = 3*x + 2 ;
    return ans ;
}

// double 
double d(double y ){
    return y/2 ; 
}

int doubleToInt(double y){
    return floor(y); 
}
int main(){
    int test = f(4);
    printf("%d\n",test);
    double test2 = d(4.0);
    printf("%f\n",test2);
    int test3 = doubleToInt(4.5);
    printf("%d\n",test3);
    return 0 ;
}