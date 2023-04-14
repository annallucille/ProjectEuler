#include <stdio.h>

int fib(int,int);
int even(int);

int main(){
    int value = fib(1,1);
    printf("%d,", value);
}

int fib(int x,int y){
    static int value = 0;
    static int z = 0;
    if (x<4000000 && y<4000000){
        z=y;
        y+=x;
        x=z;
        value += even(y);
        fib(x,y);
    }
    else{
        return value;
    }
}

int even(int y){
    if(y%2==0){
        return y;
    }
    else{
        return 0;
    }
}