'''
(Problem 6)

The sum of the squares of the first ten natural numbers is, The square of the sum of the first ten natural numbers is, 
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is . 
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


sum_to = 100

difference = .25*(sum_to**4) + (1/6)*(sum_to**3)-.25*(sum_to**2)-(1/6)*sum_to
print(difference)