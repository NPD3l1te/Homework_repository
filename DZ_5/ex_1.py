"""
Запросить у пользователя число N - ширина треугольника.
Вывести треугольник #1 с шириной N с помощью цикла while
"""
n = int(input('ширина'))
i = n
d = '*'
p = ''
print(d * i)
while n != 1:
    n -= 1
    i -= 1
    print(p * (n-i) + (d * i))