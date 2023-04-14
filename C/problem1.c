#include <stdio.h>


int main(){
    int value = 0;
    for(int x=0; x<1000; x++){
        if(x%3==0||x%5==0){
            value += x;
        }
    }
    printf("%d", value);
}
