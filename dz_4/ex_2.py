"""
Пользователь вводит с клавиатуры три числа в переменные a, b, c.
Найдите наибольшее число из них и запишите в переменную max.
"""
a = int(input('number_1'))
b = int(input('number_2'))
c = int(input('number_3'))

max_number = max(a,b,c)
print("Максимальное число:", max_number)