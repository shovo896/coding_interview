#include<stdio.h> 
int main(){
    int x ;
    scanf("%d",&x);

    while (x!=0){
        printf("current = %d\n",x);
        int last= x % 10 ;
        printf("%d\n",last);
        x = x / 10 ;
        printf("after removing last digit = %d\n",x);
    }
    return 0 ;
}
