'''
(Problem 10)

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

less_than = 20
primes = [2,3,5,7] 
for value in range(9,less_than,2):
    for x in primes:
        if value % x == 0: 
            break
        if(x>value**0.5):
            primes.append(value) 
            break
print(sum(primes))
