'''
(Problem 2)

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
max_fibonacci = 4000000

even_fibonacci = []
fibonacci = [] 
previous_number = 1
current_number  = 2
while current_number <= max_fibonacci:
    fibonacci.append(current_number)
    while previous_number<current_number: 
        previous_number += current_number 
        fibonacci.append(previous_number)
    current_number += previous_number 
for integer in fibonacci:
    if int(integer) % 2 == 0:
        even_fibonacci.append(integer) 
print(sum(even_fibonacci))


# alternate way

even_fibonacci = []
fibonacci = [1]

previous_number = 1
current_number  = 2

while current_number <= 4000000:
    fibonacci.append(current_number)
    new_previous_number = current_number
    current_number += previous_number
    previous_number = new_previous_number

for integer in fibonacci:
    if int(integer) % 2 == 0:
        even_fibonacci.append(integer) 

print(sum(even_fibonacci))

