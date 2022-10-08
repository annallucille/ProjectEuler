'''
(Problem 9)

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2+b^2=c^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''




max = 12

squares = []

for n in range(1,max/2):
    squares.append(n**2)

for c in squares: 
    for b in range(4, int(c**.5)):
        for a in range(3,b): 
            if c == a**2 + b**2:
                sqc = int(c)**.5
                if a + b + sqc == max: 
                    product = a*b*(sqc)
                    print(sqc)
                    print(product)