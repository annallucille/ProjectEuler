#include <stdio.h>
#include "problem3.h"
#include <stdlib.h>


long largest_prime(long);
long check_prime(long, Primes*);

void main(){
    long p = 600;
    long value = largest_prime(p);
    printf("%ld,", value);
}

Primes* add(long x,Primes*val){
    long z = check_prime(x, val);
    if(z!=0){
        Primes*new= malloc(sizeof(z));
        new -> number = z;
        val->next = new;
        new->prev = val;
        new->next = NULL;
        return new;
    }
    else{
        return NULL;
    }
}


long largest_prime(long p){
    Primes*prime=malloc(sizeof(long));
    prime -> number = 2;
    prime -> prev = NULL;
    prime -> next = NULL;
    long largestPrime = 0; 
    for(long i = 3; i<(p-1)/2; i+=2){
       Primes*new = malloc(sizeof(i));
       new = add(i,prime); 
       if(new!=NULL && new->number>largestPrime){
        largestPrime = new->number;
        prime = new;
       }
    }
    return largestPrime;
}

long check_prime(long x, Primes*val){
    if(val==NULL){
        return x;
    }
    else if(x%(val->number)!=0){
       check_prime(x,val->prev);
    }
    else{
        return 0;
    }
}