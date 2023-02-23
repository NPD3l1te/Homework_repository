import random

numbers = [random.randint(0, 200) for i in range(100)]

with open('random_numbers.txt', 'w') as f:
    for number in numbers:
        f.write(str(number) + '\n')

