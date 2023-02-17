import random

lst = [random.randint(0, 200) for i in range(100)]
print(lst)

f = open('random_numbers.txt', 'w')
f.write(f"{lst}")
