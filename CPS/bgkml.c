#include<stdio.h>
int main(){
    int x ;   //.  `eta hobe na at the end 
    scanf("%d",&x);
    int sum = 0 ;
    while(x!=0){
        int last = x % 10 ;
        sum += last ;
        printf("last %d sum= %d\n",last,sum);

        x/= 10 ;

    }
    printf("%d\n",sum);
    return 0 ;

}