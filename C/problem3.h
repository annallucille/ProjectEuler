#include <stdio.h>


typedef struct Primes{
    long number;
    struct Primes* next;
    struct Primes* prev;
}Primes;

Primes*add(long num, Primes* val);
long largest_prime(long p);
long check_prime(long x, Primes*val); 