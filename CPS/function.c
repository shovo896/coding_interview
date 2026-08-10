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
    return (int)y;
}

int f2(int x,double y){
    return x+y ;
}

int max(int a,int b){
    if (a>b){
        return a ;
    }
    else{
        return b ;
    }
}

int main(){
    int test = f(4);
    printf("%d\n",test);
    double test2 = d(4.0);
    printf("%f\n",test2);
    int test3 = doubleToInt(4.5);
    printf("%d\n",test3);
    int test4 = f2(3,5.0);
    printf("%d\n",test4);
    int test5 = max(3,5);
    printf("%d\n",test5);
    return 0 ;
}