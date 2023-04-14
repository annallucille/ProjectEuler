'''
(Problem 7)

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the 10 001st prime number?
'''


place = 99
primes=[2, 3, 5, 7, 11]
i= 5
for value in range(11, 100000000000 ,2):
    for x in primes:
        if value % x == 0:
            break 
        if(x>int(value**0.5)):
            primes.append(value)
            break
        i = len(primes)
    if (i==place+1):
        break
    
print(i)
print(max(primes))  