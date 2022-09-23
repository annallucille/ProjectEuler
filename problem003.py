'''
(Problem 3)

The prime factors of 13195 are 5, 7, 13 and 29.What is the largest prime factor of the number 600851475143
'''

large_number = 600851475143
factors = []

for odd in range(1, int(large_number**.5)+2, 2):
    if large_number % odd == 0: 
        factors.append(odd)
        large_factor = large_number / odd 
        factors.append(int(large_factor))
prime_factors = factors.copy()
for factor in factors:
    max_test = int(factor**.5)+1
    for x in range(3,max_test,2):
        if  factor % x == 0:
            prime_factors.remove(factor)
            break
print(prime_factors)