
'''
(Problem 1)

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. 
Find the sum of all the multiples of 3 or 5 below 1000.
'''

max_range = 1000
answers= []
numbers = range(1,max_range)
for number in numbers:
    if int(number) % 3 == 0 or int(number) % 5 == 0:
        answers.append(number)
print(sum(answers))