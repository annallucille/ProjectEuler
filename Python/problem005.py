'''
(Problem 5)

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

test_index = [1, 9]
max_test =  4000000000
if int(test_index[1]) <= 10:
    print("error index must be larger that [1,10]")

else: 
    example =  2520
    example_index = [1, 10]
    min_index = 1
    for n in range(1, (int(test_index[1]/2))+2):
        min_index = min_index * n
    
    goal = list(range(min_index, max_test, example*(int(test_index[1]/2)+1)))
    for current in range(min_index, max_test, example*(int(test_index[1]/2)+1)):
        for value in range(example_index[1], test_index[1]):
            if current % value != 0:
                goal.remove(current)
                break
    print(min(goal))